#!/usr/bin/env python3
"""Prediction-only rule-based baseline for a blind audit.

Reads synthetic telemetry only. It deliberately does not read event labels,
calculate evaluation metrics, or claim that an alert is a confirmed leak.
Thresholds are illustrative hypotheses, not operational settings.
"""
from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "telemetry_synthetic_5min.csv"
OUT = ROOT / "outputs"
FLOW_SURPLUS_THRESHOLD_M3H = 8.0
PRESSURE_GRADIENT_THRESHOLD_M = 12.5
SENSOR_GAP_DEVIATION_THRESHOLD_M = 3.0


def main() -> None:
    with DATA.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))

    predictions = []
    for row in rows:
        flow_surplus = float(row["inlet_flow_m3h"]) - float(row["demand_proxy_m3h"])
        pressure_gradient = (
            float(row["pressure_p01_upstream_m"])
            - float(row["pressure_p03_downstream_m"])
        )
        observed_gap = (
            float(row["pressure_p02_mid_m"])
            - float(row["pressure_p03_downstream_m"])
        )
        expected_gap = 6.0 + 0.03 * (float(row["demand_proxy_m3h"]) - 30.0)
        gap_deviation = observed_gap - expected_gap

        leak_candidate = (
            flow_surplus >= FLOW_SURPLUS_THRESHOLD_M3H
            and pressure_gradient >= PRESSURE_GRADIENT_THRESHOLD_M
        )
        sensor_fault_candidate = (
            abs(gap_deviation) >= SENSOR_GAP_DEVIATION_THRESHOLD_M
            and not leak_candidate
        )

        predictions.append({
            "timestamp_utc": row["timestamp_utc"],
            "zone_id": row["zone_id"],
            "flow_surplus_m3h": round(flow_surplus, 3),
            "pressure_gradient_m": round(pressure_gradient, 3),
            "sensor_gap_deviation_m": round(gap_deviation, 3),
            "leak_candidate": str(leak_candidate).lower(),
            "sensor_fault_candidate": str(sensor_fault_candidate).lower(),
        })

    OUT.mkdir(parents=True, exist_ok=True)
    output_path = OUT / "blind_predictions.csv"
    with output_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(predictions[0].keys()))
        writer.writeheader()
        writer.writerows(predictions)

    print(f"Telemetry rows processed: {len(rows)}")
    print(f"Prediction rows written: {len(predictions)}")
    print(f"Output: {output_path.relative_to(ROOT)}")
    print("No ground-truth labels or evaluation metrics were loaded/calculated.")


if __name__ == "__main__":
    main()
