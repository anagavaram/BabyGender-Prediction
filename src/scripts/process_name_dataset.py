import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

# Load raw data
df = pd.read_csv('data/raw/ssa_names_combined.csv')

# Aggregate across years — get total count per name+gender
agg = df.groupby(['name','gender'])['count'].sum().reset_index()

# Pivot to get M and F counts side by side
pivot = agg.pivot_table(index='name', columns='gender',
                        values='count', fill_value=0).reset_index()
pivot.columns = ['name', 'count_F', 'count_M']

# Determine dominant gender
pivot['total'] = pivot['count_F'] + pivot['count_M']
pivot['gender'] = (pivot['count_M'] > pivot['count_F']).astype(int)  # 1=Male
pivot['gender_confidence'] = pivot[['count_F','count_M']].max(axis=1) / pivot['total']

# Filter low-confidence names (optional)
pivot = pivot[pivot['gender_confidence'] >= 0.75]

# Feature engineering: name-based features
pivot['name_len'] = pivot['name'].str.len()
pivot['last_letter'] = pivot['name'].str[-1].str.lower()
pivot['last_2'] = pivot['name'].str[-2:].str.lower()
pivot['first_letter'] = pivot['name'].str[0].str.lower()
pivot['vowel_count'] = pivot['name'].str.lower().str.count('[aeiou]')
pivot['ends_in_vowel'] = pivot['name'].str[-1].str.lower().isin(list('aeiou')).astype(int)

pivot.to_csv('data/processed/names_processed.csv', index=False)
print(pivot.head())

