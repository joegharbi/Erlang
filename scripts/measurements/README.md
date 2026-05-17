# Measurement scripts

Purpose: execute benchmark workloads and append results to tracked CSV files.

Main scripts:
- `client_c*.py`: C server measurements
- `client_erlang*.py`: Erlang server measurements
- `client_java*.py`: Java server measurements
- `run_script.py`: sequential helper that runs a C, Erlang, and Java measurement script

Outputs:
- Appended CSVs in `results/benchmark_outputs/`

Notes:
- Scripts assume required runtime tools (Scaphandre, server runtimes, and binaries) are available.
- JSON captures and temporary logs from runs are generated artifacts and should remain untracked.
