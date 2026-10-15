import csv
import unittest
from datetime import datetime, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "telemetry_synthetic_5min.csv"
EVENTS = ROOT / "data" / "ground_truth_events.csv"

class SyntheticDataTests(unittest.TestCase):
    def test_expected_row_count_and_cadence(self):
        with DATA.open(newline="", encoding="utf-8") as f:
            rows = list(csv.DictReader(f))
        self.assertEqual(len(rows), 14 * 24 * 12)
        ts = [datetime.fromisoformat(r["timestamp_utc"].replace("Z", "+00:00")) for r in rows]
        self.assertTrue(all(ts[i + 1] - ts[i] == timedelta(minutes=5) for i in range(len(ts) - 1)))

    def test_no_ground_truth_or_event_labels_in_input_telemetry(self):
        with DATA.open(newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            fields = set(reader.fieldnames or [])
        forbidden = {"ground_truth_leak", "event_type", "event_id", "sensor_fault_flag", "leak_label"}
        self.assertTrue(fields.isdisjoint(forbidden))

    def test_event_intervals_are_valid_and_within_dataset(self):
        with DATA.open(newline="", encoding="utf-8") as f:
            rows = list(csv.DictReader(f))
        with EVENTS.open(newline="", encoding="utf-8") as f:
            events = list(csv.DictReader(f))
        start = datetime.fromisoformat(rows[0]["timestamp_utc"].replace("Z", "+00:00"))
        end = datetime.fromisoformat(rows[-1]["timestamp_utc"].replace("Z", "+00:00"))
        self.assertEqual(len(events), 6)
        for event in events:
            ev_start = datetime.fromisoformat(event["start_utc"].replace("Z", "+00:00"))
            ev_end = datetime.fromisoformat(event["end_utc"].replace("Z", "+00:00"))
            self.assertLess(ev_start, ev_end)
            self.assertGreaterEqual(ev_start, start)
            self.assertLessEqual(ev_end, end + timedelta(minutes=5))

    def test_basic_measurement_ranges(self):
        with DATA.open(newline="", encoding="utf-8") as f:
            rows = list(csv.DictReader(f))
        for r in rows:
            self.assertGreater(float(r["inlet_flow_m3h"]), 0)
            self.assertGreater(float(r["pressure_p01_upstream_m"]), float(r["pressure_p03_downstream_m"]) - 5)
            self.assertGreater(float(r["tank_level_m"]), 0)

if __name__ == "__main__":
    unittest.main()
