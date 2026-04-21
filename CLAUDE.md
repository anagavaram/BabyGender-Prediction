# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Baby gender prediction ML project using scikit-learn, XGBoost, and HuggingFace transformers. No UI framework has been chosen yet — the project is currently CLI/script-based.

## Build & Run Commands

```bash
# Docker (preferred — isolates all ML deps from host)
docker compose up --build ml-dev          # dev mode with live volume mounts
docker compose --profile inference up --build ml-inference  # self-contained inference
docker compose exec ml-dev bash           # shell into running container
docker compose exec ml-dev python src/main.py  # run entry point

# Local (if not using Docker)
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
python src/main.py
```

No test runner, linter, or CI pipeline is configured yet.

## Architecture

- **`src/`** — Application code. Entry point is `src/main.py` (referenced by Dockerfile).
- **`data/raw/`** — Original datasets. CSV files are gitignored.
- **`data/processed/`** — Cleaned/transformed data ready for training.
- **`models/`** — Serialized trained models (.pkl, .joblib, etc.).
- **`notebooks/`** — Jupyter notebooks for EDA and experimentation.

## Key Dependencies

- **ML**: scikit-learn, xgboost, transformers (HuggingFace)
- **Data**: pandas, numpy, pyarrow
- **Viz**: matplotlib, seaborn
- Python 3.13 (pinned in Dockerfile)

## Docker Setup

Two docker-compose services:
- `ml-dev` mounts `src/`, `data/`, `models/`, `notebooks/` as volumes for live editing
- `ml-inference` bakes everything into the image with no host mounts (activated via `--profile inference`)

`libgomp1` is installed in the image for XGBoost's OpenMP requirement.

## Data Handling

CSV files are excluded from git (`.gitignore`). Secrets go in `.env` (also gitignored). Data should be sourced externally or placed in `data/raw/` before running.
