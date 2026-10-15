#!/usr/bin/env python3
"""Transparent rule-based baseline for the synthetic smart-water case.

The thresholds are instructional hypotheses, not operational settings.
No third-party packages required.
"""
from __future__ import annotations
import csv
import json
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "telemetry_synthetic_5min.csv"
EVENTS = ROOT / "data" / "ground_truth_events.csv"
OUT = ROOT / "outputs"

FLOW_SURPLUS_THRESHOLD_M3H = 8.0
PRESSURE_GRADIENT_THRESHOLD_M = 12.5
SENSOR_GAP_DEVIATION_THRESHOLD_M = 3.0


def load_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def parse_ts(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def event_is_active(ts: datetime, event: dict[str, str]) -> bool:
    start = parse_ts(event["start_utc"])
    end = parse_ts(event["end_utc"])
    return start <= ts < end


def safe_ratio(n: int, d: int) -> float | None:
    return None if d == 0 else n / d


def main() -> None:
    data = load_csv(DATA)
    events = load_csv(EVENTS)
    leak_events = [e for e in events if e["ground_truth_leak"].lower() == "true"]
    out_rows = []
    tp = fp = tn = fn = 0
    leak_event_detected = {e["event_id"]: False for e in leak_events}
    first_alarm = {e["event_id"]: None for e in leak_events}
    sensor_fault_tp = sensor_fault_fp = 0

    for row in data:
        ts = parse_ts(row["timestamp_utc"])
        flow_surplus = float(row["inlet_flow_m3h"]) - float(row["demand_proxy_m3h"])
        pressure_gradient = float(row["pressure_p01_upstream_m"]) - float(row["pressure_p03_downstream_m"])
        observed_gap = float(row["pressure_p02_mid_m"]) - float(row["pressure_p03_downstream_m"])
        expected_gap = 6.0 + 0.03 * (float(row["demand_proxy_m3h"]) - 30.0)
        gap_deviation = observed_gap - expected_gap

        leak_candidate = flow_surplus >= FLOW_SURPLUS_THRESHOLD_M3H and pressure_gradient >= PRESSURE_GRADIENT_THRESHOLD_M
        sensor_fault_candidate = abs(gap_deviation) >= SENSOR_GAP_DEVIATION_THRESHOLD_M and not leak_candidate
        truth_leak_events = [e for e in leak_events if event_is_active(ts, e)]
        truth_leak = bool(truth_leak_events)
        truth_sensor_fault = any(e["event_type"] == "pressure_sensor_drift" and event_is_active(ts, e) for e in events)

        if leak_candidate and truth_leak:
            tp += 1
            for e in truth_leak_events:
                leak_event_detected[e["event_id"]] = True
                if first_alarm[e["event_id"]] is None:
                    first_alarm[e["event_id"]] = ts.isoformat()
        elif leak_candidate and not truth_leak:
            fp += 1
        elif not leak_candidate and truth_leak:
            fn += 1
        else:
            tn += 1

        if sensor_fault_candidate and truth_sensor_fault:
            sensor_fault_tp += 1
        elif sensor_fault_candidate and not truth_sensor_fault:
            sensor_fault_fp += 1

        out_rows.append({
            **row,
            "flow_surplus_m3h": round(flow_surplus, 3),
            "pressure_gradient_m": round(pressure_gradient, 3),
            "sensor_gap_deviation_m": round(gap_deviation, 3),
            "leak_candidate": str(leak_candidate).lower(),
            "sensor_fault_candidate": str(sensor_fault_candidate).lower(),
            "ground_truth_leak_for_evaluation_only": str(truth_leak).lower(),
        })

    precision = safe_ratio(tp, tp + fp)
    recall = safe_ratio(tp, tp + fn)
    f1 = None if precision is None or recall is None or (precision + recall) == 0 else 2 * precision * recall / (precision + recall)
    specificity = safe_ratio(tn, tn + fp)
    leak_event_recall = safe_ratio(sum(leak_event_detected.values()), len(leak_event_detected))
    sensor_fault_recall = safe_ratio(sensor_fault_tp, sum(1 for row in data if any(e["event_type"] == "pressure_sensor_drift" and event_is_active(parse_ts(row["timestamp_utc"]), e) for e in events)))

    OUT.mkdir(parents=True, exist_ok=True)
    pred_path = OUT / "baseline_predictions.csv"
    with pred_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(out_rows[0].keys()))
        writer.writeheader()
        writer.writerows(out_rows)

    metrics = {
        "status": "synthetic_baseline_only",
        "rules": {
            "flow_surplus_threshold_m3h": FLOW_SURPLUS_THRESHOLD_M3H,
            "pressure_gradient_threshold_m": PRESSURE_GRADIENT_THRESHOLD_M,
            "sensor_gap_deviation_threshold_m": SENSOR_GAP_DEVIATION_THRESHOLD_M,
        },
        "leak_point_metrics": {
            "tp": tp, "fp": fp, "tn": tn, "fn": fn,
            "precision": precision, "recall": recall, "f1": f1, "specificity": specificity,
        },
        "leak_event_metrics": {
            "number_of_leak_events": len(leak_event_detected),
            "detected_leak_events": sum(leak_event_detected.values()),
            "event_recall": leak_event_recall,
            "detected_by_event_id": leak_event_detected,
            "first_alarm_utc_by_event_id": first_alarm,
        },
        "sensor_fault_point_metrics": {
            "detected_sensor_fault_samples": sensor_fault_tp,
            "false_sensor_fault_samples": sensor_fault_fp,
            "sensor_fault_sample_recall": sensor_fault_recall,
        },
        "limitations": [
            "Rules and thresholds are illustrative and should not be used operationally.",
            "Synthetic telemetry was generated by a simplified transparent model, not calibrated using BattLeDIM or real utility measurements.",
            "The event labels are used only for offline evaluation and must not be used as detector inputs.",
            "Synthetic performance does not predict performance on real distribution networks.",
        ],
    }
    (OUT / "baseline_metrics.json").write_text(json.dumps(metrics, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps(metrics, indent=2, ensure_ascii=False))
    print(f"\nWrote {pred_path.relative_to(ROOT)} and outputs/baseline_metrics.json")


if __name__ == "__main__":
    main()
