model_card = '''
---
language: en
tags:
  - baby-names
  - gender-classification
  - sklearn
  - pediatric-growth
metrics:
  - accuracy
  - f1
---

# Baby Gender Predictor

Predicts baby gender using:
- **Name features** (length, ending letters, vowel patterns) — ~90% accuracy
- **Growth measurements** (age, height, weight, BMI) — ~70% accuracy

## Usage
```python
import joblib
model = joblib.load('name_gender_model.pkl')
```

## Datasets
- SSA Baby Names (1980–2022)
- WHO Child Growth Standards
'''

with open('models/README.md', 'w') as f:
    f.write(model_card)

