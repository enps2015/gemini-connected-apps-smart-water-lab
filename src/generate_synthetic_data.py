#!/usr/bin/env python3
"""Generate a reproducible, research-informed synthetic water-network time series.

This is a pedagogical simulator, NOT a calibrated hydraulic model and NOT real utility data.
Only Python's standard library is required.
"""
from __future__ import annotations

import csv
import math
import random
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
SEED = 20261015
START = datetime(2025, 5, 1, 0, 0, tzinfo=timezone.utc)
N_DAYS = 14
STEP_MIN = 5
N_ROWS = N_DAYS * 24 * 60 // STEP_MIN

EVENTS = [
    {
        "event_id": "EVT-001",
        "event_type": "small_leak",
        "start_utc": "2025-05-04T01:00:00Z",
        "end_utc": "2025-05-05T12:00:00Z",
        "affected_signal": "network flow and downstream pressure",
        "simulated_mechanism": "persistent unaccounted flow plus localized pressure loss",
        "ground_truth_leak": "true",
        "notes": "Illustrative low-to-moderate persistent leak; not fitted to a real utility event.",
    },
    {
        "event_id": "EVT-002",
        "event_type": "burst_leak",
        "start_utc": "2025-05-08T16:20:00Z",
        "end_utc": "2025-05-08T18:00:00Z",
        "affected_signal": "network flow and downstream pressure",
        "simulated_mechanism": "large short-duration unaccounted flow plus larger pressure loss",
        "ground_truth_leak": "true",
        "notes": "Synthetic burst interval; short event tests event sensitivity and latency.",
    },
    {
        "event_id": "EVT-003",
        "event_type": "micro_leak",
        "start_utc": "2025-05-07T01:00:00Z",
        "end_utc": "2025-05-07T03:00:00Z",
        "affected_signal": "network flow and downstream pressure",
        "simulated_mechanism": "small unaccounted flow increase and modest localized pressure loss",
        "ground_truth_leak": "true",
        "notes": "Subtle event intended to challenge a fixed-threshold detector; a miss is an expected limitation, not a data error.",
    },
    {
        "event_id": "EVT-004",
        "event_type": "pressure_sensor_drift",
        "start_utc": "2025-05-10T04:00:00Z",
        "end_utc": "2025-05-12T06:00:00Z",
        "affected_signal": "pressure_p03_downstream_m",
        "simulated_mechanism": "positive measurement drift that ramps over time; no actual leak",
        "ground_truth_leak": "false",
        "notes": "Synthetic instrument fault used to test differential diagnosis.",
    },
    {
        "event_id": "EVT-005",
        "event_type": "demand_surge",
        "start_utc": "2025-05-11T18:00:00Z",
        "end_utc": "2025-05-11T20:00:00Z",
        "affected_signal": "district demand proxy, inlet flow and all pressure points",
        "simulated_mechanism": "legitimate demand increase; pressure changes broadly but flow-demand residual remains normal",
        "ground_truth_leak": "false",
        "notes": "Synthetic confounder; tests whether the baseline confuses demand with leakage.",
    },
    {
        "event_id": "EVT-006",
        "event_type": "joint_sensor_bias",
        "start_utc": "2025-05-06T13:00:00Z",
        "end_utc": "2025-05-06T14:30:00Z",
        "affected_signal": "inlet flow meter and downstream pressure sensor",
        "simulated_mechanism": "inlet-flow reading biased high while downstream pressure reading is biased low; no true leak",
        "ground_truth_leak": "false",
        "notes": "Adversarial confounder: two simultaneous sensor biases mimic the expected leak signature.",
    },
]


def parse_utc(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def in_event(ts: datetime, event: dict) -> bool:
    return parse_utc(event["start_utc"]) <= ts < parse_utc(event["end_utc"])


def daily_demand(hour: float, weekend: bool) -> float:
    # Stylized, deliberately transparent shape: low overnight, two daytime peaks.
    morning = 8.0 * math.exp(-0.5 * ((hour - 7.5) / 1.8) ** 2)
    evening = 10.0 * math.exp(-0.5 * ((hour - 19.0) / 2.2) ** 2)
    midday = 3.0 * math.exp(-0.5 * ((hour - 13.0) / 3.0) ** 2)
    weekend_factor = 0.93 if weekend else 1.0
    return weekend_factor * (25.0 + morning + evening + midday)


def build_rows() -> list[dict]:
    rng = random.Random(SEED)
    rows = []
    for i in range(N_ROWS):
        ts = START + timedelta(minutes=STEP_MIN * i)
        hour = ts.hour + ts.minute / 60
        weekend = ts.weekday() >= 5
        demand = max(10.0, daily_demand(hour, weekend) + rng.gauss(0, 1.15))
        surge = any(e["event_type"] == "demand_surge" and in_event(ts, e) for e in EVENTS)
        if surge:
            demand += 9.0 + rng.gauss(0, 0.9)

        active_leak = [e for e in EVENTS if e["event_type"] in ("small_leak", "burst_leak", "micro_leak") and in_event(ts, e)]
        leak_extra = 0.0
        leak_pressure_loss = 0.0
        for event in active_leak:
            if event["event_type"] == "small_leak":
                leak_extra += 7.0
                leak_pressure_loss += 2.6
            elif event["event_type"] == "micro_leak":
                leak_extra += 4.0
                leak_pressure_loss += 1.6
            else:
                leak_extra += 14.0
                leak_pressure_loss += 5.4

        # A baseline unaccounted-flow term is included to mimic measurement/balance mismatch.
        baseline_loss = 2.8 + 0.3 * math.sin(2 * math.pi * hour / 24)
        inlet_flow = max(0.0, demand + baseline_loss + leak_extra + rng.gauss(0, 0.65))
        paired_bias = any(e["event_type"] == "joint_sensor_bias" and in_event(ts, e) for e in EVENTS)
        if paired_bias:
            inlet_flow += 6.5  # simulated high bias; actual network flow is unchanged

        # Simplified pressure response. These coefficients are pedagogical assumptions,
        # not hydraulic parameters estimated from BattLeDIM or any utility.
        p01 = 43.0 - 0.070 * (demand - 30.0) + rng.gauss(0, 0.25)
        p02 = 37.0 - 0.125 * (demand - 30.0) + rng.gauss(0, 0.30) - 0.55 * leak_pressure_loss
        p03_true = 31.0 - 0.155 * (demand - 30.0) + rng.gauss(0, 0.32) - leak_pressure_loss

        sensor_drift_event = next((e for e in EVENTS if e["event_type"] == "pressure_sensor_drift" and in_event(ts, e)), None)
        drift = 0.0
        if sensor_drift_event:
            elapsed_steps = int((ts - parse_utc(sensor_drift_event["start_utc"])).total_seconds() // (STEP_MIN * 60))
            drift = min(7.0, 0.055 * elapsed_steps)
        p03 = p03_true + drift
        if paired_bias:
            p03 -= 4.0  # simulated low bias; actual network pressure is unchanged

        # Tank level is a slowly varying operational signal; not used by the baseline rule.
        tank_level = 4.2 - 0.0035 * (demand - 30.0) - 0.012 * leak_extra + rng.gauss(0, 0.035)
        tank_level = min(5.0, max(2.8, tank_level))

        rows.append({
            "timestamp_utc": ts.strftime("%Y-%m-%dT%H:%M:%SZ"),
            "zone_id": "DMA-SIM-01",
            "inlet_flow_m3h": round(inlet_flow, 3),
            "demand_proxy_m3h": round(demand, 3),
            "pressure_p01_upstream_m": round(p01, 3),
            "pressure_p02_mid_m": round(p02, 3),
            "pressure_p03_downstream_m": round(p03, 3),
            "tank_level_m": round(tank_level, 3),
            "pump_state": "ON" if (hour >= 5.5 and hour < 23.5) else "CYCLING",
        })
    return rows


def write_csv(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    rows = build_rows()
    write_csv(DATA_DIR / "telemetry_synthetic_5min.csv", rows)
    write_csv(DATA_DIR / "ground_truth_events.csv", EVENTS)
    print(f"Generated {len(rows)} rows at {STEP_MIN}-minute cadence with seed={SEED}.")
    print("Files: data/telemetry_synthetic_5min.csv and data/ground_truth_events.csv")
    print("Reminder: the series is synthetic and not calibrated to a real water network.")


if __name__ == "__main__":
    main()
