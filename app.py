from diffusers import StableDiffusionXLPipeline
import torch, random, os

# Load model from local safetensors file
pipeline = StableDiffusionXLPipeline.from_single_file(f"models/any-sdxl-model.safetensors")

# Adjust pipeline input parameters
prompt = "A beautiful sunset over a mountain range, high resolution photograph"
negative_prompt = "cartoon, anime, unrealistic, low resolution, low quality"
iterations = 3
guidance = 7
width = 768
height = 1024
seed = None

# Generate a random seed if none is provided, initialize generator with seed
if seed is None:
    seed = random.randint(0, 2**32 - 1)
generator = torch.Generator().manual_seed(seed)

# Set device type and precision
device = "cuda" if torch.cuda.is_available() else "cpu"
precision = torch.float16 if device == "cuda" else torch.float32
pipeline = pipeline.to(device=device, dtype=precision)

# Generate an image from pipeline and define it as the output
output = pipeline(
    prompt=prompt,
    negative_prompt=negative_prompt,
    num_inference_steps=iterations,
    guidance_scale=guidance,
    width=width,
    height=height,
    generator=generator
)

# Define output directory and ensure it exists using os
os.makedirs("outputs", exist_ok=True)

# Generate unique filename with the seed and an incrementing value
filename = next(
    (f"outputs/{seed}-{i}.png" for i in range(1, 1000)
     if not os.path.exists(f"outputs/{seed}-{i}.png")),
    f"outputs/{seed}.png"
)
output.images[0].save(filename)
print(f"Image saved to {filename}")
