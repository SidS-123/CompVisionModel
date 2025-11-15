import gradio as gr
from transformers import pipeline
import os

# Model selection: prefer HUB model id (configurable via env var `MODEL_ID`).
# If a local folder named `canid-skull-classifier` exists, it will be used instead.
DEFAULT_HF_MODEL = os.environ.get("MODEL_ID", "sidAIstuff/canid-skull-classifier")
local_model_folder = os.path.join(os.path.dirname(__file__), "canid-skull-classifier")

if os.path.isdir(local_model_folder):
    model_source = local_model_folder
else:
    model_source = DEFAULT_HF_MODEL

# Load image classification pipeline from the selected source
classifier = pipeline("image-classification", model=model_source)

# Define a prediction function
def predict(image):
    preds = classifier(image)
    # Format nicely: label and confidence
    return {p["label"]: round(p["score"], 3) for p in preds}

# Create Gradio interface
app = gr.Interface(
    fn=predict,
    inputs=gr.Image(type="filepath", label="Upload a Canid Skull Image"),
    outputs=gr.Label(label="Predicted Species"),
    title="🦴 Canid Skull Classifier",
    description="Upload a skull image to see the predicted species."
    ,
    # Enable local flagging: users can "Flag" examples. Saved to the `flagged/` folder.
    allow_flagging="manual",
    flagging_dir="flagged"
)

# Launch locally
if __name__ == "__main__":
    app.launch()
