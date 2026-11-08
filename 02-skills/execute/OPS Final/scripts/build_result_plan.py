#!/usr/bin/env python3
"""Tạo kế hoạch ghi metric đã xác minh. Không gọi API hoặc ghi Google Sheet."""

import argparse
import json
from collections import Counter
from pathlib import Path


def text(value, field):
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{field}: cần chuỗi không rỗng")
    return value.strip()


def build_plan(data):
    if data.get("run_complete") is not True:
        raise ValueError("Lần chạy chưa hoàn tất; không tạo kế hoạch ghi N/A")
    sheet = data.get("sheet_name")
    if sheet not in ("Sales_by_variant", "Sales_by_product"):
        raise ValueError("sheet_name phải là Sales_by_variant hoặc Sales_by_product")
    metrics = data.get("metrics")
    results = data.get("results")
    if not isinstance(metrics, list) or not metrics:
        raise ValueError("Cần danh sách metric đọc từ Sheet")
    if not isinstance(results, list) or not results:
        raise ValueError("Không có kết quả; kiểm tra console/script trước khi ghi")

    by_name = {}
    used_rows = set()
    for metric in metrics:
        name = text(metric.get("name"), "metric.name")
        row = metric.get("row")
        if type(row) is not int or row < 2:
            raise ValueError("row phải là số dòng Sheet từ 2 trở đi")
        key = name.casefold()
        if key in by_name or row in used_rows:
            raise ValueError(f"Dòng/tên metric trùng: {name}; cần xác minh mapping")
        by_name[key] = {"row": row, "metric": name}
        used_rows.add(row)

    checks = {}
    for result in results:
        name = text(result.get("metric"), "result.metric")
        key = name.casefold()
        if key not in by_name:
            raise ValueError(f"Metric chưa map vào Sheet: {name}")
        status = result.get("status")
        if status not in ("Passed", "Failed"):
            raise ValueError(f"Status không hợp lệ của {name}: {status}")
        if key in checks and data.get("subchecks_verified") is not True:
            raise ValueError(f"Nhiều kết quả cho {name}; cần xác minh subcheck/cùng run")
        if status == "Failed":
            message = result.get("message")
            text(message, "Failed.message")
        else:
            message = None
        checks.setdefault(key, []).append((status, message))

    cells = []
    for key, metric in sorted(by_name.items(), key=lambda item: item[1]["row"]):
        observed = checks.get(key, [])
        failures = [message for status, message in observed if status == "Failed"]
        status = "Failed" if failures else "Passed" if observed else "N/A"
        # Giữ nguyên thông báo lỗi, chỉ bỏ dòng trùng hoàn toàn.
        note = "\n".join(dict.fromkeys(failures)) if failures else None
        cells.append({**metric, "value": status, "note": note})
    counts = Counter(cell["value"] for cell in cells)
    return {
        "sheet_name": sheet,
        "cells": cells,
        "counts": {status: counts[status] for status in ("Passed", "Failed", "N/A")},
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    try:
        data = json.loads(args.input.read_text(encoding="utf-8"))
        if not isinstance(data, dict):
            raise ValueError("Input phải là JSON object")
        plan = build_plan(data)
    except (ValueError, TypeError, AttributeError, OSError) as error:
        parser.exit(1, f"Chưa tạo kế hoạch: {error}\n")
    # Không tạo hoặc ghi đè output nếu input chưa hợp lệ.
    args.output.write_text(json.dumps(plan, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Đã tạo kế hoạch {plan['sheet_name']}: {plan['counts']}. Chưa ghi Sheet.")


if __name__ == "__main__":
    main()
