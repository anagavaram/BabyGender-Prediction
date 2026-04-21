import pandas as pd
import requests, zipfile, io, os

# WHO growth data is available at:
# https://www.who.int/tools/child-growth-standards/standards
# Download weight-for-age tables
who_urls = {
    'wfa_boys': 'https://cdn.who.int/media/docs/default-source/child-growth/child-growth-standards/indicators/weight-for-age/wfa_boys_0-to-5-years_zscores.xlsx',
    'wfa_girls': 'https://cdn.who.int/media/docs/default-source/child-growth/child-growth-standards/indicators/weight-for-age/wfa_girls_0-to-5-years_zscores.xlsx'
}

# Or use the NHANES dataset from CDC for real measurements
# Download from: https://wwwn.cdc.gov/nchs/nhanes/
# DEMO: create synthetic WHO-based dataset
import numpy as np

np.random.seed(42)
n = 5000
ages = np.random.randint(0, 60, n)  # months
genders = np.random.choice([0, 1], n)  # 0=F, 1=M

# Boys slightly heavier/taller after 6 months
weight = 3.5 + ages * 0.19 + genders * 0.3 * (ages > 6) + np.random.normal(0, 0.8, n)
height = 50 + ages * 1.8 + genders * 0.5 * (ages > 6) + np.random.normal(0, 2.0, n)

growth_df = pd.DataFrame({'age_months': ages, 'gender': genders,
                           'weight_kg': weight, 'height_cm': height})
growth_df['bmi'] = growth_df['weight_kg'] / (growth_df['height_cm']/100)**2
growth_df.to_csv('data/raw/growth_data.csv', index=False)

