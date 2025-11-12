from huggingface_hub import upload_folder

# 🔧 Replace with your Hugging Face username and repo name
repo_id = "sidAIstuff/canid-skull-classifier"
folder_path = r"C:\\Users\\16367\\OneDrive\\Desktop\\CANID_SKULL_PROJECT\\canid-skull-classifier\\model"

import os

# Replace with your Hugging Face repo id (username/repo-name)
repo_id = "sidAIstuff/canid-skull-classifier"

# The local folder that contains your model artifacts. AutoTrain created
# the folder `canid-skull-classifier` in the project root (contains
# config.json, model.safetensors, etc.). We upload that folder.
local_dir = os.path.join(os.path.dirname(__file__), "canid-skull-classifier")

if not os.path.isdir(local_dir):
    raise SystemExit(f"Local model folder not found: {local_dir}")

print(f"Uploading folder '{local_dir}' to '{repo_id}' on the Hub...")
upload_folder(
    folder_path=local_dir,
    path_in_repo='.',
    repo_id=repo_id,
    repo_type='model',
    commit_message='Upload AutoTrain model',
)

print("✅ Model uploaded successfully!")
