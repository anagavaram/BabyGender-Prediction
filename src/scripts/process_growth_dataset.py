import pandas as pd
import numpy as np

df = pd.read_csv('data/raw/growth_data.csv')

# Drop nulls
df = df.dropna(subset=['age_months','weight_kg','height_cm','gender'])

# Feature engineering
df['bmi'] = df['weight_kg'] / (df['height_cm'] / 100) ** 2
df['age_group'] = pd.cut(df['age_months'],
                          bins=[0,3,6,12,24,36,48,60],
                          labels=['0-3m','3-6m','6-12m','1-2y','2-3y','3-4y','4-5y'])
df['weight_per_cm'] = df['weight_kg'] / df['height_cm']

# Normalize features
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
features = ['age_months','weight_kg','height_cm','bmi','weight_per_cm']
df[features] = scaler.fit_transform(df[features])

import joblib
joblib.dump(scaler, 'models/growth_scaler.pkl')

df.to_csv('data/processed/growth_processed.csv', index=False)
print(df.shape)

