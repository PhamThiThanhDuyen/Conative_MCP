#!/usr/bin/env python3
"""Validate SKILL.md context size against Conative and OpenAI limits."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


WARNING_WORDS = 800
WARNING_LINES = 150
MAX_WORDS = 5_000
MAX_LINES = 500


def skill_body(text: str) -> str:
    """Return the Markdown body without YAML frontmatter."""
    if not text.startswith("---"):
        return text
    match = re.match(r"^---\r?\n.*?\r?\n---\r?\n?", text, re.DOTALL)
    return text[match.end() :] if match else text


def collect_skill_files(inputs: list[str]) -> list[Path]:
    files: set[Path] = set()
    for raw in inputs:
        path = Path(raw)
        if path.is_file():
            if path.name == "SKILL.md":
                files.add(path.resolve())
            continue
        if path.is_dir():
            direct = path / "SKILL.md"
            if direct.is_file():
                files.add(direct.resolve())
            else:
                files.update(item.resolve() for item in path.rglob("SKILL.md"))
    return sorted(files)


def measure(path: Path) -> tuple[int, int]:
    body = skill_body(path.read_text(encoding="utf-8"))
    words = len(re.findall(r"\S+", body))
    lines = len(body.splitlines())
    return words, lines


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Warn on large skills and fail only at OpenAI context limits."
    )
    parser.add_argument(
        "paths",
        nargs="*",
        default=["02-skills"],
        help="SKILL.md files, skill directories, or roots to scan",
    )
    parser.add_argument(
        "--fail-on-warning",
        action="store_true",
        help="Return exit code 2 when warnings exist and no hard failure exists",
    )
    args = parser.parse_args()

    skill_files = collect_skill_files(args.paths)
    if not skill_files:
        print("ERROR: No SKILL.md files found", file=sys.stderr)
        return 1

    warnings = 0
    failures = 0
    for path in skill_files:
        words, lines = measure(path)
        if words > MAX_WORDS or lines > MAX_LINES:
            status = "FAIL"
            failures += 1
        elif words > WARNING_WORDS or lines > WARNING_LINES:
            status = "WARN"
            warnings += 1
        else:
            status = "PASS"
        print(f"[{status}] {path}: {words} words, {lines} lines")

    print(
        f"Summary: {len(skill_files)} skills, {warnings} warning(s), "
        f"{failures} failure(s)"
    )
    if failures:
        return 1
    if warnings and args.fail_on_warning:
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
