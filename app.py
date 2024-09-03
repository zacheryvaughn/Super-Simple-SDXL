from diffusers import StableDiffusionXLPipeline
import torch
import os

# Options and parameters
model = "any-sdxl-model.safetensors"
prompt = "A beautiful sunset over a mountain range, high resolution photograph"
negative_prompt = "cartoon, anime, unrealistic, low resolution, low quality"
num_inference_steps = 20
guidance_scale = 7
width = 768
height = 1024
generator = None

# Load model from local safetensors file
pipeline = StableDiffusionXLPipeline.from_single_file(f"models/{model}")

# Set device and precision
device = "cuda" if torch.cuda.is_available() else "cpu"
precision = torch.float16 if device == "cuda" else torch.float32
pipeline = pipeline.to(device=device, dtype=precision)

# Generate and save an image with additional parameters
output = pipeline(
    prompt=prompt, 
    negative_prompt=negative_prompt, 
    num_inference_steps=num_inference_steps, 
    guidance_scale=guidance_scale, 
    width=width, 
    height=height, 
    generator=generator
)

# Make sure "outputs" directory exists, then save the generated image
os.makedirs("outputs", exist_ok=True)
output.images[0].save("outputs/image.png")
print(f"Image saved to outputs/image.png")
