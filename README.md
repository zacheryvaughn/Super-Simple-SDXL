# Super Simple SDXL Text-to-Image Inference
#### Simplest method for running SDXL from a single stafetensors file (on MacOS)
I hope this will help anyone who wants to get started generating images locally with any fine-tuned SDXL .safetensors model. This relies entirely on the [HuggingFace Diffusers library](https://huggingface.co/docs/diffusers/en/index) with their [SDXL Pipeline](https://huggingface.co/docs/diffusers/en/using-diffusers/sdxl), all I am doing is providing you a very basic inference starting point. These instructions assume you are on M1 Mac and already have Homebrew, Python, XCode, and an IDE. People seem to be having issues using from_single_file, but it's usually because they're using an incompatible file, the wrong pipeline, or an invalid path, you can absolutely use a single .safetensors file and this is how.

## Step 1: Setup your project directory structure.
models/ (directory containing your models)<bg>
outputs/ (directory where generated images will go)<bg>
app.py (inference script for generating images)<bg>
requirements.txt (for tracking dependencies)

## Step 2: Create a virtual environment in your root directory.
In terminal:<bg>
python3 -m venv .venv


## Step 3: Activate your virtual environment.
In terminal:<bg>
source myenv/bin/activate


## Step 4: Make sure pip is up to date.
In terminal:<bg>
pip install --upgrade pip


## Step 5: Install the Hugging Face Diffusers library.
In terminal:<bg>
pip install diffusers


## Step 6: Install the Transformers library.
In terminal:<bg>
pip install transformers


## Step 7: Update your requirements.txt file.
In terminal:<bg>
pip freeze > requirements.txt


## Step 8: Write your app.py script.
Copy my script. Make sure to put your safetensors in the models directory.<bg>
Add the model file name at the top of your script adjust the parameters.

## Step 9: Run your script.
In terminal:<bg>
python app.py

## Disclaimer

This project uses the [Hugging Face Diffusers library](https://github.com/huggingface/diffusers) and [Stable Diffusion XL (SDXL) models](https://huggingface.co/models). 

- **Hugging Face Diffusers Library**: The Diffusers library is provided by Hugging Face and is licensed under the [Apache License 2.0](https://opensource.org/licenses/Apache-2.0). I do not own the rights to this library.

- **Stable Diffusion XL (SDXL) Models**: The SDXL models are also provided by Hugging Face and may be subject to their respective licenses. I do not own the rights to these models.

For more information about their licenses and usage, please refer to the official documentation and license agreements provided by Hugging Face.

This project is not affiliated with, endorsed by, or sponsored by Hugging Face or StabilityAI.
