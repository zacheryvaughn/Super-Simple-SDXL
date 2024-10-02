# Super Simple SDXL Text-to-Image Inference
#### This is the bare minimum script for running SDXL with the Diffusers library from Hugging Face.
#### Only standard schedulers without sde or karras, no loRAs, and no mps precision optimizations.

## Step 1: Setup your project directory structure.
models/ (directory containing your models)  
outputs/ (directory where generated images will go)  
app.py (inference script for generating images)  
requirements.txt (for tracking dependencies)

## Step 2: Create a virtual environment in your root directory.
In terminal:  
python3 -m venv .venv


## Step 3: Activate your virtual environment.
In terminal:  
source .venv/bin/activate


## Step 4: Make sure pip is up to date.
In terminal:  
pip install --upgrade pip


## Step 5: Install the Hugging Face Diffusers library.
In terminal:  
pip install diffusers


## Step 6: Install the Transformers library.
In terminal:  
pip install transformers


## Step 7: Install the Transformers library.
In terminal:  
pip install torch


## Step 8: Update your requirements.txt file.
In terminal:  
pip freeze > requirements.txt


## Step 8: Write your app.py script.
Copy my script. Make sure to put your safetensors in the models directory.  
Add the model file name in the parameters section at the top.

## Step 9: Run your script.
In terminal:  
python app.py

#### Side node: 1024x1024 with Euler generates at around 2 iteration per minute on M1 Mac. You can add manual precision handling for mps in this to make it run up to 4X faster.
