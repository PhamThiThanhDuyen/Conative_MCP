# -*- coding: utf-8 -*-
import unittest
from copy import deepcopy

from build_list_result_plan import build_list_plan


def fixture():
    return {
        "sheet_name": "Sales_by_variant",
        "requests": ["List_Variant/Variant_List_Product_Info", "List_Variant/Test_Sales"],
        "finalize": False,
        "distinct_items_verified": {"List_Variant/Variant_List_Product_Info": True, "List_Variant/Test_Sales": True},
        "metrics": [{"row": 3, "name": "Variant Title"}, {"row": 24, "name": "Total Sales"}, {"row": 51, "name": "Ad spend"}],
        "pages": [{"request": "List_Variant/Variant_List_Product_Info", "offset": n, "script_offset": n, "limit": 20, "items_checked": 20, "run_complete": True,
                   "results": [{"metric": "Variant Title", "status": "Failed", "message": "❌ Test giả lập: sai title"}] if n == 20 else [{"metric": "Variant Title", "status": "Passed"}]}
                  for n in (0, 20, 40, 60, 80)],
    }


class ListPlanTests(unittest.TestCase):
    def test_partial_has_no_na_and_keeps_early_red(self):
        plan = build_list_plan(fixture())
        self.assertEqual(len(plan["cells"]), 1)
        self.assertEqual(plan["cells"][0]["value"], "Failed")
        self.assertIn("offset: 20\n❌ Test giả lập: sai title", plan["cells"][0]["note"])
        self.assertEqual(plan["counts"]["N/A"], 0)

    def test_final_needs_all_folder_apis(self):
        data = fixture()
        data["finalize"] = True
        with self.assertRaisesRegex(ValueError, "mọi API"):
            build_list_plan(data)

    def test_later_green_preserves_failed_and_final_missing_is_na(self):
        data = fixture()
        data["finalize"] = True
        pages = deepcopy(data["pages"])
        for page in pages:
            page["request"] = data["requests"][1]
            page["results"] = [{"metric": "Variant Title", "status": "Passed"}, {"metric": "Total Sales", "status": "Passed"}]
        data["pages"].extend(pages)
        plan = build_list_plan(data)
        self.assertEqual(plan["counts"], {"Passed": 1, "Failed": 1, "N/A": 1})
        self.assertIn("offset: 20", plan["cells"][0]["note"])

    def test_missing_page_or_failed_runtime_blocks(self):
        for failure in ("missing", "runtime", "short", "duplicate", "coverage", "empty", "offset_mismatch"):
            data = fixture()
            if failure == "missing":
                data["pages"].pop()
            elif failure == "runtime":
                data["pages"][2]["run_complete"] = False
            elif failure == "short":
                data["pages"][4]["items_checked"] = 7
            elif failure == "duplicate":
                data["pages"].append(deepcopy(data["pages"][0]))
            elif failure == "coverage":
                data["distinct_items_verified"] = {}
            elif failure == "offset_mismatch":
                data["pages"][1]["script_offset"] = 0
            else:
                data["pages"][3]["results"] = []
            with self.subTest(failure=failure), self.assertRaises(ValueError):
                build_list_plan(data)

    def test_product_plan_uses_product_rows(self):
        data = fixture()
        data["sheet_name"] = "Sales_by_product"
        data["metrics"][0] = {"row": 3, "name": "Product Title"}
        for page in data["pages"]:
            for result in page["results"]:
                result["metric"] = "Product Title"
        plan = build_list_plan(data)
        self.assertEqual(plan["sheet_name"], "Sales_by_product")
        self.assertEqual(plan["cells"][0]["metric"], "Product Title")


if __name__ == "__main__":
    unittest.main()
