# Gemini Connected Apps × Smart Water Anomaly Lab — Blind Audit Snapshot

This branch (`argon-blind-audit`) is a **limited snapshot for an initial, independent code review** using Gemini 4 Argon and the connected apps.

## Purpose

Review a small, transparent rule-based detector for potential anomalies in **synthetic** water-network telemetry. The reviewer should infer limitations from the available inputs and code rather than being shown the event labels or precomputed performance metrics.

## Files intentionally included

- `data/telemetry_synthetic_5min.csv`: 4,032 synthetic measurements at five-minute intervals.
- `data/data_dictionary.csv`: schema, units, meanings and limitations.
- `src/baseline_detector.py`: a prediction-only baseline; it reads telemetry and writes predictions without reading ground-truth labels.
- `tests/test_data.py`: tests for telemetry schema, row count, five-minute cadence and separation of the input columns from labels.

## Important boundary

All telemetry in this branch is synthetic and pedagogical. It is not calibrated against a real utility network and must not be used for operational decisions. Thresholds are illustrative hypotheses, not recommended settings.

This branch intentionally excludes the event ground-truth file, baseline metric outputs, generator with event definitions, previous analysis reports and the full project documentation to reduce answer leakage during the initial audit. The complete source project and reproducibility documentation remain on the `main` branch.

## Run locally

Requires Python 3.10+ and only the standard library.

```bash
python src/baseline_detector.py
python -m unittest discover -s tests -v
```

The detector writes `outputs/blind_predictions.csv`. This branch does not calculate accuracy or compare its predictions to event labels.

## Review request

Inspect the available files. Explain what the detector does, identify assumptions and blind spots supported by exact file paths, and propose tests. Do not claim access to excluded files. Do not invent ground truth, code execution or metrics.