#!/usr/bin/env python3
"""Render a verified Claude status snapshot; no network access or writeback."""

import argparse
import json
import re
from pathlib import Path


def label(value, context):
    if not isinstance(value, str) or not value.strip() or "\n" in value or "\r" in value:
        raise ValueError(f"{context}: expected a nonempty single-line string")
    return value.strip()


def counts(values, context):
    if not isinstance(values, list):
        raise ValueError(f"{context}: missing or invalid cell-status array")
    result = {"pass": 0, "fail": 0, "blank": 0, "unknown": []}
    for value in values:
        if value is None or value == "":
            result["blank"] += 1
        elif not isinstance(value, str):
            raise ValueError(f"{context}: status must be text or null")
        elif value == "PASSED":
            result["pass"] += 1
        elif value == "FAILED":
            result["fail"] += 1
        else:
            result["unknown"].append(label(value, context))
    result["total"] = result["pass"] + result["fail"]
    return result


def rollup(statuses):
    return "FAIL" if "FAIL" in statuses else "PASS" if "PASS" in statuses else "NOT RUN"


def grain_status(value):
    return "FAIL" if value["fail"] else "PASS" if value["pass"] else "NOT RUN"


def ticket_id(value):
    value = str(value).strip().removeprefix("#")
    if not re.fullmatch(r"\d+", value):
        raise ValueError("Bug ID must be a decimal OP ticket ID")
    return str(int(value))


def collect_bug_evidence(data, organizations, titles):
    cases = data.get("testcases")
    if not isinstance(cases, list):
        raise ValueError("testcases evidence is required; rescan current Actual/Note columns")
    scopes = {(o["name"], s["name"]): s["status"]
              for o in organizations for s in o["sources"]}
    bugs, seen, gaps, unlinked = {}, set(), [], {}
    for case in cases:
        org = label(case.get("org"), "testcase org")
        source = label(case.get("source"), "testcase source")
        tc = label(case.get("tc_id"), "testcase ID")
        if not re.fullmatch(r"T2-COV-\d+", tc):
            raise ValueError(f"Invalid testcase ID: {tc}")
        key = (org, source, tc)
        if key in seen or (org, source) not in scopes:
            raise ValueError(f"Duplicate or out-of-scope testcase: {key}")
        seen.add(key)
        actual = label(case.get("actual"), f"{tc} Actual")
        if actual != "FAIL":
            continue  # An old ticket reference is not current failure evidence.
        failure = label(case.get("failure_evidence"), f"{tc} failure evidence")
        raw_ids = case.get("ticket_ids", [])
        raw_excluded = case.get("excluded_ticket_ids", [])
        if not isinstance(raw_ids, list) or not isinstance(raw_excluded, list):
            raise ValueError(f"{tc}: ticket IDs must be arrays")
        explicit = {ticket_id(i) for i in raw_ids}
        excluded = {ticket_id(i) for i in raw_excluded}
        if not excluded.issubset(explicit):
            raise ValueError(f"{tc}: excluded ticket must preserve an explicit reference")
        if excluded:
            gaps.append(label(case.get("limitation"), f"{tc} excluded-link limitation"))
            if data["bug_scan_complete"]:
                raise ValueError(f"{tc}: unresolved ticket link requires incomplete scan status")
        accepted = {i: {"link_type": "explicit"} for i in sorted(explicit - excluded)}
        matches = case.get("matched_tickets", [])
        if not isinstance(matches, list):
            raise ValueError(f"{tc}: matched_tickets must be an array")
        for match in matches:
            linked = ticket_id(match.get("ticket_id", ""))
            reason = label(match.get("reason"), f"{tc} defect-match reason")
            ref = label(match.get("ticket_reference"), f"{tc} ticket reference")
            if not ref.startswith("https://devtak.cbidigital.com/") or not re.search(
                r"/work_packages/" + re.escape(linked) + r"(?:/|$|[?#])", ref
            ):
                raise ValueError(f"{tc}: match reference does not identify ticket {linked}")
            if explicit and linked not in explicit:
                raise ValueError(f"{tc}: cannot silently reassign a different explicit ticket")
            if linked in excluded:
                raise ValueError(f"{tc}: an unresolved link cannot also be confirmed")
            accepted.setdefault(linked, {"link_type": "defect-match", "reason": reason,
                                        "ticket_reference": ref})
        if not accepted:
            unlinked.setdefault((org, source), []).append(tc)
        for linked, proof in accepted.items():
            bug = bugs.setdefault(linked, {"title": titles.get(linked), "orgs": set(),
                                          "evidence": []})
            bug["orgs"].add(org)
            bug["evidence"].append({"org": org, "source": source, "tc_id": tc,
                                    "actual": actual, "failure_evidence": failure, **proof})
        if accepted and scopes[(org, source)] != "FAIL":
            gaps.append(f"{org}/{source}/{tc}: testcase FAIL có bug; Field compare chưa phản ánh lỗi này.")
    for (org, source), tc_ids in unlinked.items():
        gaps.append(f"Chưa xác nhận ticket cho {org}/{source}: " + ", ".join(tc_ids))
    return bugs, gaps


def prepare(data):
    if not isinstance(data, dict):
        raise ValueError("Input must be a JSON object")
    organizations = data.get("organizations")
    if not isinstance(organizations, list) or not organizations:
        raise ValueError("organizations must be a nonempty array")
    if type(data.get("bug_scan_complete")) is not bool:
        raise ValueError("bug_scan_complete must be explicitly true or false")
    result, names = [], set()
    for org in organizations:
        name = label(org.get("name"), "organization name")
        if name in names:
            raise ValueError(f"Duplicate organization: {name}")
        names.add(name)
        sources = org.get("sources")
        if not isinstance(sources, list) or not sources:
            raise ValueError(f"{name}: sources must be a nonempty array")
        source_names, source_results = set(), []
        for source in sources:
            source_name = label(source.get("name"), f"{name} source name")
            if source_name in source_names:
                raise ValueError(f"{name}: duplicate source {source_name}")
            source_names.add(source_name)
            product = counts(source.get("product"), f"{name}/{source_name}/Product")
            variant = counts(source.get("variant"), f"{name}/{source_name}/Variant")
            if len(source["product"]) != len(source["variant"]):
                raise ValueError(f"{name}/{source_name}: unequal field-row coverage")
            status = rollup([grain_status(product), grain_status(variant)])
            source_results.append({"name": source_name, "product": product, "variant": variant, "status": status})
        result.append({"name": name, "sources": source_results, "status": rollup([s["status"] for s in source_results])})
    titles = {}
    for bug in data.get("bugs", []):
        ticket = ticket_id(bug.get("id", ""))
        title = bug.get("title")
        title = label(title, f"Bug {ticket} title") if title is not None else None
        if title and titles.get(ticket) and title != titles[ticket]:
            raise ValueError(f"Bug {ticket}: conflicting verified titles")
        titles[ticket] = title or titles.get(ticket)
    bugs, evidence_gaps = collect_bug_evidence(data, result, titles)
    limitations = data.get("limitations", [])
    if not isinstance(limitations, list):
        raise ValueError("limitations must be an array")
    limitations = list(dict.fromkeys([label(x, "limitation") for x in limitations] + evidence_gaps))
    if not data["bug_scan_complete"] and not limitations:
        raise ValueError("Incomplete bug scan requires a precise limitation")
    return result, bugs, limitations


def source_status(status):
    return {"PASS": "🟢 PASS", "FAIL": "🔴 FAIL"}.get(status, status)


def render(data):
    orgs, bugs, limitations = prepare(data)
    lines = ["- TỔNG QUAN"]
    for org in orgs:
        lines.append(f"  - ORG: {org['name']} - {org['status']}")
        lines.extend(f"    - Source: {s['name']} - {source_status(s['status'])}" for s in org["sources"])
    lines.append("- CHI TIẾT:")
    for org in orgs:
        lines.append(f"  - ORG: {org['name']} - {org['status']}")
        for source in org["sources"]:
            lines.append(f"    - Source: {source['name']} - {source_status(source['status'])}")
            for grain in ("Product", "Variant"):
                c = source[grain.lower()]
                lines.append(f"      - {grain}: TOTAL: {c['total']} fields")
                for key, display in (("pass", "PASS"), ("fail", "FAIL")):
                    if c[key]:
                        lines.append(f"        - {display}: {c[key]} fields")
                if not c["total"]:
                    lines.append("        - NOT RUN")
                if c["blank"]:
                    lines.append(f"        - CHƯA CÓ STATUS: {c['blank']} fields")
                if c["unknown"]:
                    tokens = ", ".join(dict.fromkeys(c["unknown"]))
                    lines.append(f"        - STATUS CHƯA NHẬN DIỆN: {len(c['unknown'])} fields ({tokens})")
    lines.append("- BUGS:")
    for ticket, bug in bugs.items():
        lines.append(f"  - {ticket} - {bug['title'] or 'Chưa xác minh title'}")
        affected = " / ".join(o["name"] for o in orgs if o["name"] in bug["orgs"])
        lines.append(f"    - ORG: {affected}")
    if not bugs:
        lines.append("  - Không có ticket OP được ghi nhận trong phạm vi báo cáo" if data["bug_scan_complete"] else "  - Chưa đủ dữ liệu để tổng hợp ticket OP")
    lines.extend(f"  - Giới hạn: {item}" for item in limitations)
    return "\n".join(lines) + "\n"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    try:
        report = render(json.loads(args.input.read_text(encoding="utf-8")))
    except (ValueError, TypeError, KeyError, AttributeError) as exc:
        parser.error(str(exc))
    if args.output:
        args.output.write_text(report, encoding="utf-8")
    else:
        print(report, end="")


if __name__ == "__main__":
    main()
