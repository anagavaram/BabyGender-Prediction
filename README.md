# Baby Gender Prediction

Machine learning project that predicts baby gender from name features and growth measurements using scikit-learn, XGBoost, and HuggingFace transformers.

## Project Structure

```
src/
├── scripts/          — Data download and processing
│   ├── download_name_dataset.py
│   ├── download_growth_dataset.py
│   ├── process_name_dataset.py
│   └── process_growth_dataset.py
├── train/            — Model training and ensemble
│   ├── train_name_gender_classifier
│   ├── train_growth_gender_classifier
│   └── build_model_ensemble.py
└── upload/           — HuggingFace model upload
    ├── upload_all_files.py
    ├── upload_hf.py
    └── model_card.py
data/raw/             — Original datasets
data/processed/       — Cleaned and transformed data
models/               — Trained model artifacts (not in git)
```

## Setup

### Docker (recommended)

```bash
docker compose up --build ml-dev
```

### Local

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Training the Models

Model files are too large for git. You must train them locally before running inference.

### Step 1: Download datasets

```bash
# SSA baby names (download names.zip manually from the URL below and save to data/raw/ssa_names/)
# https://www.ssa.gov/oact/babynames/names.zip
python src/scripts/download_name_dataset.py

# Synthetic growth data (generated automatically)
python src/scripts/download_growth_dataset.py
```

### Step 2: Process datasets

```bash
python src/scripts/process_name_dataset.py
python src/scripts/process_growth_dataset.py
```

This produces:
- `data/processed/names_processed.csv` — 86k+ names with engineered features
- `data/processed/growth_processed.csv` — 5k growth records with scaled features
- `models/growth_scaler.pkl` — StandardScaler for growth inference

### Step 3: Train models

```bash
python src/train/train_name_gender_classifier
python src/train/train_growth_gender_classifier
```

This produces:
- `models/name_gender_model.pkl` — Random Forest name classifier (~86% accuracy)
- `models/name_encoders.pkl` — Label encoders for name features
- `models/growth_gender_model.pkl` — Gradient Boosting growth classifier

### Step 4: Verify ensemble

```bash
python src/train/build_model_ensemble.py --name Emma
python src/train/build_model_ensemble.py --age 12 --weight 9.5 --height 75
```

## Running Inference

```bash
# Predict by name
python src/train/build_model_ensemble.py --name Sophia

# Predict by growth measurements (age in months, weight in kg, height in cm)
python src/train/build_model_ensemble.py --age 24 --weight 12 --height 85

# Both at once
python src/train/build_model_ensemble.py --name Sophia --age 24 --weight 12 --height 85
```

### Docker inference (self-contained image)

```bash
docker compose --profile inference up --build ml-inference
```

## Pre-trained Models

Pre-trained models are available on HuggingFace:
https://huggingface.co/anagavaram/baby-gender-predictor

## Key Dependencies

| Library | Purpose |
|---------|---------|
| scikit-learn | Classical ML models and preprocessing |
| xgboost | Gradient boosted tree models |
| transformers | HuggingFace model hub integration |
| pandas / numpy | Data manipulation |
| matplotlib / seaborn | Visualization |

## Data

CSV files are excluded from version control. The SSA names dataset requires manual download from ssa.gov (automated requests are blocked). Growth data is synthetically generated.

## License

This project is for personal/educational use.
