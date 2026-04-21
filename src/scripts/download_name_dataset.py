import pandas as pd
import requests, zipfile, io, os, sys

SSA_URL = 'https://www.ssa.gov/oact/babynames/names.zip'
RAW_DIR = 'data/raw/ssa_names'
OUTPUT_CSV = 'data/raw/ssa_names_combined.csv'

os.makedirs(RAW_DIR, exist_ok=True)

zip_path = os.path.join(RAW_DIR, 'names.zip')

if not os.path.exists(zip_path):
    print(f'Downloading from {SSA_URL}...')
    r = requests.get(SSA_URL, headers={'User-Agent': 'Mozilla/5.0'})
    if r.status_code != 200 or b'PK' not in r.content[:4]:
        print(f'Download failed (HTTP {r.status_code}). SSA blocks automated requests.')
        print(f'Please download manually:')
        print(f'  1. Open {SSA_URL} in your browser')
        print(f'  2. Save the zip file to {zip_path}')
        print(f'  3. Re-run this script')
        sys.exit(1)
    with open(zip_path, 'wb') as f:
        f.write(r.content)
    print('Download complete.')
else:
    print(f'Using existing {zip_path}')

with zipfile.ZipFile(zip_path) as z:
    z.extractall(RAW_DIR)

dfs = []
for year in range(1980, 2024):
    f = os.path.join(RAW_DIR, f'yob{year}.txt')
    if os.path.exists(f):
        df = pd.read_csv(f, names=['name', 'gender', 'count'])
        df['year'] = year
        dfs.append(df)

names_df = pd.concat(dfs, ignore_index=True)
names_df.to_csv(OUTPUT_CSV, index=False)
print(f'Loaded {len(names_df):,} records across {len(dfs)} years -> {OUTPUT_CSV}')
