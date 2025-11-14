import requests
import gradio as gr
from io import BytesIO
from PIL import Image

API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-2-1"
HF_TOKEN = "YOUR_HF_API_KEY"

headers = {"Authorization": f"Bearer {HF_TOKEN}"}

def generate_image(prompt):
    payload = {"inputs": prompt}
    response = requests.post(API_URL, headers=headers, json=payload)

    if response.status_code != 200:
        return f"Error: {response.text}"

    image_bytes = response.content
    image = Image.open(BytesIO(image_bytes))
    return image

demo = gr.Interface(
    fn=generate_image,
    inputs=gr.Textbox(label="Enter your prompt"),
    outputs=gr.Image(type="pil"),
    title="Text-to-Image with HuggingFace API",
)

demo.launch()
import requests
import gradio as gr
from io import BytesIO
from PIL import Image

API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-2-1"
HF_TOKEN = "YOUR_HF_API_KEY"

headers = {"Authorization": f"Bearer {HF_TOKEN}"}

def generate_image(prompt):
    payload = {"inputs": prompt}
    response = requests.post(API_URL, headers=headers, json=payload)

    if response.status_code != 200:
        return f"Error: {response.text}"

    image_bytes = response.content
    image = Image.open(BytesIO(image_bytes))
    return image

demo = gr.Interface(
    fn=generate_image,
    inputs=gr.Textbox(label="Enter your prompt"),
    outputs=gr.Image(type="pil"),
    title="Text-to-Image with HuggingFace API",
)

demo.launch()
