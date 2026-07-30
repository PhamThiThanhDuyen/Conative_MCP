#!/usr/bin/env python3
"""Validate Conative API verification report structure."""

from __future__ import annotations

import re
import sys
from pathlib import Path


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")


REQUIRED_SECTIONS = [
    "scope",
    "environment",
    "endpoint",
    "verification matrix",
    "evidence",
    "findings",
    "residual risks",
    "go / no-go",
]

SECRET_RE = re.compile(
    r"(?i)(authorization:\s*bearer\s+[a-z0-9._-]{8,}|password\s*[:=]\s*[^|\s]{4,}|token\s*[:=]\s*[^|\s]{8,}|secret\s*[:=]\s*[^|\s]{8,})"
)


def validate(path: Path) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []

    if not path.exists():
        return [f"File not found: {path}"], warnings

    text = path.read_text(encoding="utf-8", errors="replace")
    normalized = text.casefold()

    for section in REQUIRED_SECTIONS:
        if section not in normalized:
            errors.append(f"Missing required section/concept: {section}")

    for keyword in ["confirmed", "observed", "assumed", "blocked"]:
        if keyword not in normalized:
            warnings.append(f"Evidence state '{keyword}' not found; confirm requirement uncertainty is tracked")

    for keyword in ["auth", "schema", "error", "security", "performance", "contract"]:
        if keyword not in normalized:
            warnings.append(f"Coverage area '{keyword}' not found; confirm it is out of scope if omitted")

    if SECRET_RE.search(text):
        errors.append("Possible secret/token/password in report; sanitize evidence before handoff")

    if "owner" not in normalized:
        errors.append("Missing owner/action ownership")

    if "build" not in normalized and "version" not in normalized:
        errors.append("Missing build/version evidence")

    return errors, warnings


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("Usage: validate_api_verification_report.py <report.md>", file=sys.stderr)
        return 2

    path = Path(argv[1])
    errors, warnings = validate(path)
    print(f"\n{path}")
    for message in errors:
        print(f"ERROR: {message}")
    for message in warnings:
        print(f"WARNING: {message}")
    if not errors and not warnings:
        print("OK: API verification report checks passed")
    elif not errors:
        print("OK WITH WARNINGS")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
