# Erlang/C/Java Echo Benchmark Repository

This repository contains a long-running research benchmark setup used to compare C, Erlang, and Java echo servers under client load, with power measurements from Scaphandre on Windows.

## Repository layout

- `benchmarks/` source code for benchmark servers and Erlang modules
- `scripts/measurements/` measurement runners that execute workloads and append CSV outputs
- `scripts/analysis/` post-processing scripts for normalized tables and ratios
- `scripts/legacy/` older exploratory scripts kept for historical context
- `results/benchmark_outputs/` tracked CSV outputs used in analysis and publications
- `results/legacy_measurements/` historical raw reports and archived copies from older runs
- `docs/` informal notes and references collected during the project

## Reproducibility notes

- Keep publication-related CSV files under `results/benchmark_outputs/`.
- Keep historical reports under `results/legacy_measurements/`.
- New temporary run artifacts (JSON captures, ad-hoc logs) should not be committed.
- Measurement scripts are Windows/Scaphandre oriented and expect the required tools installed.

## Current status

The repository is active for benchmark maintenance and reproducibility, with older materials preserved in clearly labeled legacy folders.
