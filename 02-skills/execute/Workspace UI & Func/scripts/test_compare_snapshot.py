"""Synthetic checks; no live account, customer payload or writeback."""
import copy
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from compare_snapshot import compare


ROOT = Path(__file__).resolve().parents[1]


class CompareSnapshotTests(unittest.TestCase):
    def setUp(self):
        self.data = json.loads((ROOT / "assets/comparison-input.example.json").read_text())

    def test_same_numbers_different_row_order_and_scale(self):
        result = compare(self.data)
        self.assertEqual(result["status"], "PASSED")
        self.assertEqual(result["counts"], {"match": 6, "mismatch": 0, "blocked": 0})

    def test_rounding_is_visible(self):
        self.data["ui_rows"][0]["gross_sales"] = "1000"
        result = compare(self.data)
        self.assertEqual(result["status"], "FAILED")
        self.assertEqual(result["differences"][0]["id"], "QA-101")
        self.assertEqual(result["differences"][0]["ui_minus_log"], "-0.25")

    def test_missing_or_mismatched_timezone_blocks_before_value_comparison(self):
        for value in (None, "Asia/Ho_Chi_Minh"):
            with self.subTest(value=value):
                self.data["log_scope"]["timezone"] = value
                self.data["ui_rows"][0]["gross_sales"] = "999"
                result = compare(self.data)
                self.assertEqual(result["status"], "BLOCK")
                self.assertEqual(result["counts"]["mismatch"], 0)

    def test_duplicate_id_is_invalid(self):
        self.data["ui_rows"].append(copy.deepcopy(self.data["ui_rows"][0]))
        with self.assertRaisesRegex(ValueError, "duplicate UI ID"):
            compare(self.data)

    def test_incomplete_pagination_cannot_establish_missing_product(self):
        self.data["log_rows"].pop()
        self.data["log_window_complete"] = False
        self.assertEqual(compare(self.data)["status"], "BLOCK")
        self.data["log_window_complete"] = True
        self.assertEqual(compare(self.data)["status"], "FAILED")

    def test_percent_is_not_implicitly_scaled(self):
        self.data["log_rows"][1]["return_rate"] = "0.02"
        self.assertEqual(compare(self.data)["status"], "FAILED")

    def test_unknown_precision_and_missing_value_are_blocked(self):
        for value in ("1K", None):
            with self.subTest(value=value):
                self.data["ui_rows"][0]["gross_sales"] = value
                self.assertEqual(compare(self.data)["status"], "BLOCK")
        del self.data["ui_rows"][0]["gross_sales"]
        self.assertEqual(compare(self.data)["status"], "BLOCK")

    def test_failure_survives_another_blocked_field(self):
        self.data["ui_rows"][0]["gross_sales"] = "999"
        self.data["ui_rows"][0]["title"] = None
        self.assertEqual(compare(self.data)["status"], "FAILED")

    def test_title_and_grouping_are_not_normalized_without_permission(self):
        self.data["ui_rows"][0]["title"] = "Synthetic-A"
        self.assertEqual(compare(self.data)["status"], "FAILED")
        self.data["ui_rows"][0]["title"] = "Synthetic A"
        del self.data["fields"][0]["grouping_separator"]
        self.assertEqual(compare(self.data)["status"], "BLOCK")

    def test_wrong_conversation_turn_or_unverified_link_blocks(self):
        for field, value in (("conversation_id", "another-conversation"),
                             ("response_turn", "another-turn"),
                             ("response_link_verified", False),
                             ("observation_name", "model.messages")):
            with self.subTest(field=field):
                data = copy.deepcopy(self.data)
                data["log_provenance"][field] = value
                data["ui_rows"][0]["gross_sales"] = "999"
                result = compare(data)
                self.assertEqual(result["status"], "BLOCK")
                self.assertEqual(result["counts"]["mismatch"], 0)

    def test_missing_observation_blocks(self):
        del self.data["log_provenance"]["observation_id"]
        self.assertEqual(compare(self.data)["status"], "BLOCK")

    def test_legacy_qe_snapshot_cannot_pass_as_log(self):
        legacy = json.loads(json.dumps(self.data).replace('"log_', '"qe_').replace('"log"', '"qe"'))
        result = compare(legacy)
        self.assertEqual(result["status"], "BLOCK")
        self.assertIn("legacy QE snapshot", result["limitations"][0])

    def test_cli_writes_output_and_returns_status_codes(self):
        with tempfile.TemporaryDirectory() as directory:
            source, output = Path(directory) / "in.json", Path(directory) / "out.json"
            for expected, expected_code in (("PASSED", 0), ("FAILED", 1), ("BLOCK", 2)):
                if expected == "FAILED":
                    self.data["ui_rows"][0]["gross_sales"] = "999"
                if expected == "BLOCK":
                    del self.data["log_scope"]["timezone"]
                source.write_text(json.dumps(self.data))
                proc = subprocess.run([sys.executable, str(ROOT / "scripts/compare_snapshot.py"),
                                       str(source), "--output", str(output)], capture_output=True)
                self.assertEqual(proc.returncode, expected_code, proc.stderr)
                self.assertEqual(json.loads(output.read_text())["status"], expected)
            source.write_text("invalid-json")
            proc = subprocess.run([sys.executable, str(ROOT / "scripts/compare_snapshot.py"),
                                   str(source)], capture_output=True)
            self.assertEqual(proc.returncode, 2)
            self.assertEqual(json.loads(proc.stdout)["status"], "BLOCK")


if __name__ == "__main__":
    unittest.main()
