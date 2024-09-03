# Super-Simple-SDXL
I hope this will help anyone who wants to get started generating images locally with any fine-tuned SDXL .safetensors model. This relies entirely on the HuggingFace Diffusers library with their SDXL Pipeline, all I am doing is providing you a very basic inference starting point. These instructions assume you are on Mac and already have Homebrew, Python, XCode, and an IDE. People seem to be having issues using from_single_file, but it's usually because they're using an incompatible file, the wrong pipeline, or a invalid path. You can absolutely use a single .safetensors file and this is how.

# Step 1: Setup your project directory structure.
models/ (directory containing your models)
outputs/ (directory where generated images will go)
app.py (inference script for generating images)
requirements.txt (for tracking dependencies)

# Step 2: Create a virtual environment in your root directory.
In terminal:
python3 -m venv .venv


# Step 3: Activate your virtual environment.
In terminal:
source myenv/bin/activate


# Step 4: Make sure pip is up to date.
In terminal:
pip install --upgrade pip


# Step 5: Install the Hugging Face Diffusers library.
In terminal:
pip install diffusers


# Step 6: Install the Transformers library.
In terminal:
pip install transformers


# Step 7: Update your requirements.txt file.
In terminal:
pip freeze > requirements.txt


# Step 8: Write your app.py script.
Copy my script. Make sure to put your safetensors in the models directory.
Add the model file name at the top of your script adjust the parameters.

# Step 9: Run your script.
In terminal:
python app.py

