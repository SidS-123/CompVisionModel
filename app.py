import gradio as gr
from transformers import pipeline
import gradio as gr
from transformers import pipeline
import os

# Load your trained model (AutoTrain saved it to the project folder `canid-skull-classifier`)
# Adjust path if you moved the model artifacts
model_path = os.path.join(os.path.dirname(__file__), "canid-skull-classifier")

# Load image classification pipeline
classifier = pipeline("image-classification", model=model_path)

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
)

# Launch locally
if __name__ == "__main__":
    app.launch()
