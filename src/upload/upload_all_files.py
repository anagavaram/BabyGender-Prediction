import os
import glob
from huggingface_hub import HfApi

REPO_ID = 'anagavaram/baby-gender-predictor'

api = HfApi()

# Upload model card
api.upload_file(
    path_or_fileobj='models/README.md',
    path_in_repo='README.md',
    repo_id=REPO_ID,
    repo_type='model'
)
print('Uploaded: README.md')

# Upload all model files
model_files = glob.glob('models/*.pkl')
for filepath in model_files:
    filename = os.path.basename(filepath)
    api.upload_file(
        path_or_fileobj=filepath,
        path_in_repo=filename,
        repo_id=REPO_ID,
        repo_type='model'
    )
    print(f'Uploaded: {filename}')

print(f'\nModel live at: https://huggingface.co/{REPO_ID}')
