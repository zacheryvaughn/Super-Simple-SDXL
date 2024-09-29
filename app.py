import torch, random, os
from diffusers import StableDiffusionXLPipeline
from diffusers.schedulers import EulerDiscreteScheduler

# SET DEVICE AND PRECISION
if torch.cuda.is_available():
    device = "cuda"
    precision = torch.float16
elif torch.backends.mps.is_available():
    device = "mps"
    precision = torch.float32
else:
    device = "cpu"
    precision = torch.float32

# INPUT GENERATION SETTINGS
model = "EpicRealismXL-V8-KiSS.safetensors"
prompt = "A beautiful sunset over a mountain range, high resolution photograph"
negative_prompt = "cartoon, anime, unrealistic, low resolution, low quality"
iterations = 25
guidance = 5
width = 768
height = 1024
seed = None

# GENERATE SEED IF NOT IS PROVIDED
if seed is None:
    seed = random.randint(0, 2**32 - 1)
generator = torch.Generator().manual_seed(seed)

# INITIALIZE PIPELINE WITH MODEL, DEVICE, SCHEDULER
pipeline = StableDiffusionXLPipeline.from_single_file(f"models/{model}", use_safetensors=True)
pipeline = pipeline.to(device=device, dtype=precision)
pipeline.scheduler = EulerDiscreteScheduler.from_config(pipeline.scheduler.config)

# CALL THE PIPELINE TO PRODUCE AN OUTPUT
output = pipeline(
    prompt=prompt,
    negative_prompt=negative_prompt,
    num_inference_steps=iterations,
    guidance_scale=guidance,
    width=width,
    height=height,
    generator=generator
)

# ENSURE OUTPUT DIRECTORY AND SET FILENAME
os.makedirs("outputs", exist_ok=True)
filename = next(
    (f"outputs/{seed}-{i}.png" for i in range(1, 1000)
     if not os.path.exists(f"outputs/{seed}-{i}.png")),
    f"outputs/{seed}.png"
)
output.images[0].save(filename)
print(f"Image saved to {filename}")
