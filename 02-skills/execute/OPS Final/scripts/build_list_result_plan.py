#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gộp kết quả các API List đã đủ 5 trang. Không chạy API hoặc ghi Sheet."""

import argparse
import json
from collections import Counter
from pathlib import Path

from build_result_plan import build_plan, text


def build_list_plan(data):
    requests = data.get("requests")
    pages = data.get("pages")
    finalize = data.get("finalize")
    if type(finalize) is not bool:
        raise ValueError("Cần finalize true/false")
    if not isinstance(requests, list) or not requests:
        raise ValueError("Cần danh sách mọi API trong folder")
    names = [text(name, "request") for name in requests]
    if len(set(names)) != len(names):
        raise ValueError("API trùng; dùng tên/path duy nhất")
    if not isinstance(pages, list) or not pages:
        raise ValueError("Chưa có trang List hoàn tất")
    seen = {}
    results = []
    for page in pages:
        request = page.get("request")
        offset = page.get("offset")
        if request not in names:
            raise ValueError("API của trang không có trong danh sách folder")
        if type(offset) is not int or offset not in (0, 20, 40, 60, 80):
            raise ValueError("Offset phải là 0, 20, 40, 60, 80")
        if type(page.get("script_offset")) is not int or page["script_offset"] != offset:
            raise ValueError("Offset query và script chưa khớp")
        offsets = seen.setdefault(request, set())
        if offset in offsets:
            raise ValueError("Trùng API/offset; không trộn retry")
        offsets.add(offset)
        if page.get("run_complete") is not True:
            raise ValueError("Trang chưa hoàn tất; chưa tạo kế hoạch ghi")
        if type(page.get("limit")) is not int or page["limit"] != 20:
            raise ValueError("Limit mỗi trang phải là 20")
        if type(page.get("items_checked")) is not int or page["items_checked"] != 20:
            raise ValueError("Trang chưa kiểm tra đủ 20 item; cần hỏi người dùng")
        checks = page.get("results")
        if not isinstance(checks, list) or not checks:
            raise ValueError("Trang không có kết quả kiểm tra; chưa được ghi N/A")
        for check in checks:
            result = dict(check)
            if result.get("status") == "Failed":
                message = result.get("message")
                text(message, "Failed.message")
                result["message"] = f"API: {request} | offset: {offset}\n{message}"
            results.append(result)
    for request, offsets in seen.items():
        if offsets != {0, 20, 40, 60, 80}:
            raise ValueError(f"API {request} chưa đủ 5 trang")
        if data.get("distinct_items_verified", {}).get(request) is not True:
            raise ValueError(f"Chưa xác minh 100 item khác nhau của {request}")
    if finalize and set(seen) != set(names):
        raise ValueError("Chưa hoàn tất mọi API trong folder; chưa chốt N/A")
    plan = build_plan({
        "run_complete": True,
        "sheet_name": data.get("sheet_name"),
        "metrics": data.get("metrics"),
        "subchecks_verified": True,
        "results": results,
    })
    if not finalize:
        plan["cells"] = [cell for cell in plan["cells"] if cell["value"] != "N/A"]
    counts = Counter(cell["value"] for cell in plan["cells"])
    plan["counts"] = {status: counts[status] for status in ("Passed", "Failed", "N/A")}
    plan.update(mode="List", finalize=finalize, completed_requests=[n for n in names if n in seen])
    return plan


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    try:
        data = json.loads(args.input.read_text(encoding="utf-8"))
        plan = build_list_plan(data)
    except (ValueError, TypeError, AttributeError, OSError) as error:
        parser.exit(1, f"Chưa tạo kế hoạch List: {error}\n")
    args.output.write_text(json.dumps(plan, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Đã tạo kế hoạch List: {plan['counts']}. Chưa ghi Sheet.")


if __name__ == "__main__":
    main()
