import csv
import unittest
from datetime import datetime, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "telemetry_synthetic_5min.csv"

class BlindAuditInputTests(unittest.TestCase):
    def setUp(self):
        with DATA.open(newline="", encoding="utf-8") as handle:
            self.reader = csv.DictReader(handle)
            self.fields = self.reader.fieldnames or []
            self.rows = list(self.reader)

    def test_expected_schema_and_row_count(self):
        expected = [
            "timestamp_utc", "zone_id", "inlet_flow_m3h", "demand_proxy_m3h",
            "pressure_p01_upstream_m", "pressure_p02_mid_m",
            "pressure_p03_downstream_m", "tank_level_m", "pump_state"
        ]
        self.assertEqual(self.fields, expected)
        self.assertEqual(len(self.rows), 14 * 24 * 12)

    def test_five_minute_timestamp_cadence(self):
        ts = [datetime.fromisoformat(row["timestamp_utc"].replace("Z", "+00:00")) for row in self.rows]
        self.assertTrue(all(ts[i + 1] - ts[i] == timedelta(minutes=5) for i in range(len(ts) - 1)))

    def test_input_has_no_label_columns(self):
        forbidden = {"ground_truth_leak", "event_type", "event_id", "sensor_fault_flag", "leak_label"}
        self.assertTrue(set(self.fields).isdisjoint(forbidden))

    def test_core_numeric_fields_parse(self):
        for row in self.rows:
            for field in (
                "inlet_flow_m3h", "demand_proxy_m3h", "pressure_p01_upstream_m",
                "pressure_p02_mid_m", "pressure_p03_downstream_m", "tank_level_m"
            ):
                float(row[field])

if __name__ == "__main__":
    unittest.main()
