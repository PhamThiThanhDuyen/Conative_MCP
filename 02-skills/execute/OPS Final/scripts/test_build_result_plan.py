import unittest
from copy import deepcopy

from build_result_plan import build_plan


def fixture():
    return {
        "run_complete": True,
        "sheet_name": "Sales_by_variant",
        "metrics": [
            {"row": 18, "name": "Gross Sales"},
            {"row": 24, "name": "Total Sales"},
            {"row": 51, "name": "Ad spend"},
        ],
        "results": [
            {"metric": "Gross Sales", "status": "Passed"},
            {"metric": "Total Sales", "status": "Failed", "message": "❌ Test giả lập total_sales: A=10, B=12, Difference=2"},
        ],
    }


class ResultPlanTests(unittest.TestCase):
    def test_completed_run_maps_pass_fail_missing_and_preserves_note(self):
        data = fixture()
        original = deepcopy(data)
        plan = build_plan(data)
        self.assertEqual(plan["counts"], {"Passed": 1, "Failed": 1, "N/A": 1})
        self.assertEqual([cell["row"] for cell in plan["cells"]], [18, 24, 51])
        self.assertEqual(plan["cells"][1]["note"], data["results"][1]["message"])
        self.assertIsNone(plan["cells"][2]["note"])
        self.assertEqual(data, original)

    def test_incomplete_run_never_becomes_all_na(self):
        data = fixture()
        data["run_complete"] = False
        with self.assertRaisesRegex(ValueError, "chưa hoàn tất"):
            build_plan(data)

    def test_empty_console_is_blocked(self):
        data = fixture()
        data["results"] = []
        with self.assertRaisesRegex(ValueError, "Không có kết quả"):
            build_plan(data)

    def test_unknown_metric_is_not_silently_na(self):
        data = fixture()
        data["results"][0]["metric"] = "Unmapped sales"
        with self.assertRaisesRegex(ValueError, "chưa map"):
            build_plan(data)

    def test_failed_requires_note(self):
        data = fixture()
        data["results"][1].pop("message")
        with self.assertRaisesRegex(ValueError, "Failed.message"):
            build_plan(data)

    def test_duplicate_row_or_name_is_blocked(self):
        for metric in ({"row": 18, "name": "Other"}, {"row": 99, "name": "TOTAL SALES"}):
            data = fixture()
            data["metrics"].append(metric)
            with self.assertRaisesRegex(ValueError, "trùng"):
                build_plan(data)

    def test_mixed_results_need_verified_subchecks(self):
        data = fixture()
        data["results"].append({"metric": "Total Sales", "status": "Passed"})
        with self.assertRaisesRegex(ValueError, "subcheck"):
            build_plan(data)
        data["subchecks_verified"] = True
        self.assertEqual(build_plan(data)["cells"][1]["value"], "Failed")

    def test_product_has_its_own_metric_rows(self):
        data = fixture()
        data["sheet_name"] = "Sales_by_product"
        data["metrics"][1]["row"] = 21
        self.assertEqual(build_plan(data)["cells"][1]["row"], 21)

    def test_no_write_to_other_tab_or_status(self):
        data = fixture()
        data["sheet_name"] = "Danh sách org"
        with self.assertRaises(ValueError):
            build_plan(data)
        data = fixture()
        data["results"][0]["status"] = "PASS"
        with self.assertRaises(ValueError):
            build_plan(data)


if __name__ == "__main__":
    unittest.main()
