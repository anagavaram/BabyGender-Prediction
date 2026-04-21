# Baby Gender Prediction

Machine learning project that predicts baby gender based on prenatal features using scikit-learn, XGBoost, and HuggingFace transformers.

## Project Structure

```
src/            — Application and model code (entry point: main.py)
data/raw/       — Original datasets
data/processed/ — Cleaned and transformed data
models/         — Trained model artifacts
notebooks/      — Jupyter notebooks for EDA and experimentation
```

## Setup

### Docker (recommended)

```bash
docker compose up --build ml-dev
```

This mounts `src/`, `data/`, `models/`, and `notebooks/` as live volumes — code changes reflect instantly without rebuilding.

### Local

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python src/main.py
```

## Running Inference

```bash
# Self-contained image with all data and models baked in
docker compose --profile inference up --build ml-inference
```

## Key Dependencies

| Library | Purpose |
|---------|---------|
| scikit-learn | Classical ML models and preprocessing |
| xgboost | Gradient boosted tree models |
| transformers | HuggingFace model hub integration |
| pandas / numpy | Data manipulation |
| matplotlib / seaborn | Visualization |

## Data

CSV files are excluded from version control. Place your dataset in `data/raw/` before running. Processed outputs are written to `data/processed/`.

## License

This project is for personal/educational use.
