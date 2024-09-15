import requests
import gradio as gr
from PIL import Image
import io
import os

# API settings
API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-3-medium-diffusers"
headers = {"Authorization": f"Bearer {os.getenv('HF_API_KEY')}"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.content

def generate_room_plan(prompt):
    image_bytes = query({"inputs": prompt})
    
    # Convert the byte content to an image
    image = Image.open(io.BytesIO(image_bytes))
    
    return image

with gr.Blocks() as app:
    gr.Markdown("# Space Plan Generator")

    with gr.Row():
        user_prompt = gr.Textbox(label="Enter your prompt for the space plan")

    output = gr.Image(label="Generated Space Plan")

    gr.Button("Generate Space Plan").click(
        generate_room_plan,
        inputs=[user_prompt],
        outputs=output
    )

app.launch() 
