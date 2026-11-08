#!/usr/bin/env python3
"""Compare minimal, verified UI/log snapshots offline; never call a live service."""

import argparse
from decimal import Decimal, InvalidOperation
import json
from pathlib import Path
import re


SCOPE_KEYS = ("org_id", "grain", "sources", "from", "to", "timezone",
              "date_boundary", "filters")
NUMBER = re.compile(r"^[+-]?(?:\d+(?:\.\d*)?|\.\d+)$")
GROUPED = re.compile(r"^[+-]?\d{1,3}(?:,\d{3})+(?:\.\d+)?$")


def numeric(value, field):
    if isinstance(value, bool) or not isinstance(value, (str, int, Decimal)):
        raise ValueError("numeric value must be a decimal string or integer")
    raw = str(value).strip()
    if field["type"] == "percent" and raw.endswith("%"):
        raw = raw[:-1].strip()  # Same percentage unit, never multiply/divide by 100.
    if "," in raw and field.get("grouping_separator") == "," and GROUPED.fullmatch(raw):
        raw = raw.replace(",", "")
    if not NUMBER.fullmatch(raw):
        raise ValueError("unverified numeric precision, unit or locale")
    number = Decimal(raw)
    if not number.is_finite():
        raise ValueError("non-finite numeric value")
    return number


def index_rows(rows, key, side):
    if not isinstance(rows, list):
        raise ValueError(f"{side}_rows must be a list")
    result = {}
    for row in rows:
        if not isinstance(row, dict) or not isinstance(row.get(key), str) or not row[key]:
            raise ValueError(f"{side} needs a nonempty string ID in {key}")
        if row[key] in result:
            raise ValueError(f"duplicate {side} ID: {row[key]}")
        result[row[key]] = row
    return result


def compare(data):
    result = {"case_id": data.get("case_id"), "status": "BLOCK",
              "counts": {"match": 0, "mismatch": 0, "blocked": 0},
              "fields": {}, "differences": [], "limitations": []}

    def block(reason):
        result["limitations"].append(reason)
        result["counts"]["blocked"] += 1

    legacy = any(key.startswith("qe_") for key in data)
    legacy = legacy or "qe" in data.get("key", {}) or any(
        isinstance(field, dict) and "qe" in field for field in data.get("fields", []))
    if legacy:
        block("legacy QE snapshot is not Langfuse evidence; capture the matching log")
        return result

    provenance = data.get("log_provenance", {})
    required = ("conversation_id", "session_id", "trace_id", "observation_id",
                "observation_name", "response_turn")
    for key in required:
        if not isinstance(provenance.get(key), str) or not provenance[key].strip():
            block(f"missing log provenance: {key}")
    if provenance.get("observation_name") != "tool.execution:query_data":
        block("log observation must be tool.execution:query_data")
    for ui_key, log_key in (("ui_conversation_id", "conversation_id"),
                            ("ui_response_turn", "response_turn")):
        if not isinstance(data.get(ui_key), str) or not data[ui_key].strip():
            block(f"missing UI provenance: {ui_key}")
        elif data[ui_key] != provenance.get(log_key):
            block(f"log provenance mismatch: {log_key}")
    if provenance.get("response_link_verified") is not True:
        block("matching UI response, tenant and query linkage not verified")
    if result["limitations"]:
        return result

    for key in dict.fromkeys((*SCOPE_KEYS, *data.get("required_scope", []))):
        left, right = data.get("ui_scope", {}), data.get("log_scope", {})
        if key not in left or key not in right or left[key] in (None, "") or right[key] in (None, ""):
            block(f"missing scope: {key}")
        elif left[key] != right[key]:
            block(f"scope mismatch: {key}")
    if result["limitations"]:
        return result  # Different scopes cannot establish a field-value failure.

    fields = data.get("fields", [])
    if not isinstance(fields, list) or not fields:
        block("no verified fields supplied")
        return result
    for field in fields:
        if not all(isinstance(field.get(k), str) and field[k] for k in ("ui", "log", "type")):
            raise ValueError("each field needs ui, log and type strings")
        if field["type"] not in ("decimal", "percent", "string"):
            raise ValueError("supported field types: decimal, percent, string")
        if field["ui"] in result["fields"]:
            raise ValueError("duplicate UI field mapping")
        result["fields"][field["ui"]] = {"match": 0, "mismatch": 0, "blocked": 0}
    keys = data["key"]
    ui = index_rows(data["ui_rows"], keys["ui"], "UI")
    log = index_rows(data["log_rows"], keys["log"], "log")
    if not ui:
        block("no UI rows; empty-report assertions require separate evidence")
        return result
    for item_id, row in ui.items():
        if item_id not in log:
            state = "mismatch" if data.get("log_window_complete") is True else "blocked"
            result["counts"][state] += 1
            result["differences"].append({"id": item_id, "field": "__row__", "state": state,
                                           "reason": "UI ID absent from collected log window"})
            continue
        for field in fields:
            a, b = field["ui"], field["log"]
            entry = {"id": item_id, "field": a, "log_field": b}
            try:
                if a not in row or b not in log[item_id]:
                    raise ValueError("missing value; not zero")
                left, right = row[a], log[item_id][b]
                entry.update(ui=left, log=right)
                if left is None or right is None:
                    if not (left is None and right is None and field.get("nulls_equal") is True):
                        raise ValueError("null semantics not verified")
                elif field["type"] == "string":
                    if not isinstance(left, str) or not isinstance(right, str):
                        raise ValueError("string values required")
                else:
                    left, right = numeric(left, field), numeric(right, field)
                    entry["ui_minus_log"] = str(left - right)
                state = "match" if left == right else "mismatch"
            except (ValueError, InvalidOperation) as exc:
                state = "blocked"
                entry["reason"] = str(exc)
            result["counts"][state] += 1
            result["fields"][a][state] += 1
            if state != "match":
                entry["state"] = state
                result["differences"].append(entry)
    counts = result["counts"]
    result["status"] = "FAILED" if counts["mismatch"] else "BLOCK" if counts["blocked"] else "PASSED"
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    try:
        data = json.loads(args.input.read_text(encoding="utf-8"), parse_float=Decimal)
        result = compare(data)
    except (OSError, ValueError, KeyError, TypeError, AttributeError) as exc:
        result = {"status": "BLOCK", "limitations": [f"invalid snapshot: {exc}"]}
    rendered = json.dumps(result, indent=2, ensure_ascii=False, default=str) + "\n"
    if args.output:
        args.output.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")
    return {"PASSED": 0, "FAILED": 1, "BLOCK": 2}[result["status"]]


if __name__ == "__main__":
    raise SystemExit(main())
