import os
import joblib
from huggingface_hub import HfApi, create_repo

# Files to upload
model_files = [
    'models/name_gender_model.pkl',
    'models/growth_gender_model.pkl',
    'models/name_encoders.pkl',
    'models/growth_scaler.pkl',
    'models/confusion_matrix.png',
    'models/feature_importance.png',
]

REPO_ID = 'anagavaram/baby-gender-predictor'

# Create repo (set private=True if you want it private)
create_repo(REPO_ID, repo_type='model', exist_ok=True)

