#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
python3 -m pytest -q labs/01-core-patterns labs/02-state-contract
