#!/usr/bin/env bash
set -euo pipefail

# Simple entrypoint for Railway to run the d20 roller.
python_cmd="$(command -v python3 || command -v python || true)"

if [[ -z "$python_cmd" ]]; then
  echo "Python is not available on this image. Please use a Python runtime or install Python." >&2
  exit 1
fi

"$python_cmd" d20.py
