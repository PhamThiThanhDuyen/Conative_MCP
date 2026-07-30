#!/usr/bin/env python3
"""Validate Markdown manual-QA test design artifacts."""

from __future__ import annotations

import re
import sys
from pathlib import Path


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")


CASE_ID_RE = re.compile(r"^\|\s*([A-Z][A-Z0-9]*-[A-Z0-9]+-\d{3})\s*\|")
VAGUE_RE = re.compile(
    r"\b(theo policy|theo thiết kế|hoạt động đúng|xử lý đúng|nếu cần|as appropriate)\b",
    re.IGNORECASE,
)
SECRET_RE = re.compile(
    r"(?i)(password|passwd|token|secret|otp)\s*[:=]\s*(?!\$?\{?[A-Z][A-Z0-9_]*\}?)([^|\s]{4,})"
)


def pipe_count(line: str) -> int:
    return line.count("|")


def validate(path: Path) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []

    if not path.exists():
        return [f"File not found: {path}"], warnings

    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    normalized = text.casefold()

    required_concepts = {
        "equivalence partitions": ("phân vùng tương đương", "equivalence partition"),
        "boundary values": ("phân tích giá trị biên", "boundary value"),
        "decision tables": ("bảng quyết định", "decision table"),
        "test data": ("test data", "dữ liệu kiểm thử"),
        "traceability": ("traceability", "truy vết"),
        "test scenarios": ("test scenarios", "testcase", "test cases"),
    }
    for label, variants in required_concepts.items():
        if not any(v in normalized for v in variants):
            errors.append(f"Missing required section/concept: {label}")

    has_top_to_bottom = "top-to-bottom" in normalized or "từ trên xuống" in normalized
    has_left_to_right = "left-to-right" in normalized or "trái qua phải" in normalized
    if not has_top_to_bottom or not has_left_to_right:
        errors.append("Missing explicit top-to-bottom, left-to-right execution order")

    if not re.search(r"\bEP-[A-Z0-9-]+", text):
        errors.append("No equivalence-partition IDs found (expected EP-...)")
    if not re.search(r"\bBV-[A-Z0-9-]+", text):
        errors.append("No boundary-value IDs found (expected BV-...)")
    if not re.search(r"\bDT-[A-Z0-9-]+", text):
        errors.append("No decision-table IDs found (expected DT-...)")

    case_rows: list[tuple[int, str, str]] = []
    for number, line in enumerate(lines, 1):
        match = CASE_ID_RE.match(line)
        if match:
            case_rows.append((number, match.group(1), line))

    if not case_rows:
        errors.append("No testcase rows found; expected IDs like LOG-VAL-001")
    else:
        seen: dict[str, int] = {}
        for number, case_id, line in case_rows:
            if case_id in seen:
                errors.append(
                    f"Duplicate testcase ID {case_id} at lines {seen[case_id]} and {number}"
                )
            seen[case_id] = number
            vague = VAGUE_RE.search(line)
            if vague:
                errors.append(
                    f"Ambiguous expected language '{vague.group(1)}' in {case_id} at line {number}"
                )

    # Validate contiguous Markdown table column counts.
    in_table = False
    expected_pipes = 0
    table_start = 0
    for number, line in enumerate(lines, 1):
        if line.startswith("|"):
            current = pipe_count(line)
            if not in_table:
                in_table = True
                expected_pipes = current
                table_start = number
            elif current != expected_pipes:
                errors.append(
                    f"Markdown table column mismatch at line {number}: "
                    f"{current} pipes, expected {expected_pipes} from line {table_start}"
                )
        else:
            in_table = False
            expected_pipes = 0

    header_lines = [line.casefold() for line in lines if line.startswith("|")]
    has_case_technique_columns = any(
        "technique" in line and ("partition/rule" in line or "partition" in line)
        for line in header_lines
    )
    has_external_traceability = "traceability kỹ thuật" in normalized or "## 9. traceability" in normalized
    if not has_case_technique_columns and not has_external_traceability:
        errors.append("Missing technique/partition mapping in testcase schema or traceability table")

    if VAGUE_RE.search(text) and not case_rows:
        warnings.append("Document contains ambiguous language; review manually")

    for number, line in enumerate(lines, 1):
        if SECRET_RE.search(line) and "secret reference" not in line.casefold():
            warnings.append(f"Possible embedded secret at line {number}; inspect manually")

    if "blocked – awaiting requirement" not in normalized and "blocked - awaiting requirement" not in normalized:
        warnings.append("No blocked-assumption status found; confirm that all requirements are complete")

    return errors, warnings


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print("Usage: validate_testcase_design.py <file.md> [file2.md ...]", file=sys.stderr)
        return 2

    failed = False
    for raw in argv[1:]:
        path = Path(raw)
        errors, warnings = validate(path)
        print(f"\n{path}")
        for message in errors:
            print(f"ERROR: {message}")
        for message in warnings:
            print(f"WARNING: {message}")
        if not errors and not warnings:
            print("OK: manual QA design checks passed")
        elif not errors:
            print("OK WITH WARNINGS")
        failed = failed or bool(errors)

    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
