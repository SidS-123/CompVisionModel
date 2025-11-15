import os
from huggingface_hub import upload_folder

# Replace with your Hugging Face repo id (username/repo-name)
repo_id = os.environ.get("HF_REPO_ID", "sidAIstuff/canid-skull-classifier")

# The local folder that may contain model artifacts. We behave safely if it's absent.
local_dir = os.path.join(os.path.dirname(__file__), "canid-skull-classifier")

if not os.path.isdir(local_dir):
    print(f"Local model folder not found: {local_dir}")
    print("If you want to upload a model, place the model folder at that path and re-run this script.")
    raise SystemExit(0)

print(f"Uploading folder '{local_dir}' to '{repo_id}' on the Hub...")
upload_folder(
    folder_path=local_dir,
    path_in_repo='.',
    repo_id=repo_id,
    repo_type='model',
    commit_message='Upload AutoTrain model',
)

print("✅ Model uploaded successfully!")
