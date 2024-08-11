import json
from openai import OpenAI
import pandas as pd
from IPython.display import Image, display
import os

# Initializing OpenAI client - see https://platform.openai.com/docs/quickstart?context=python
client = OpenAI()

# get the openai key from .env file
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def check_and_create_folder(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"Folder '{folder_path}' created.")
    else:
        print(f"Folder '{folder_path}' already exists.")
check_and_create_folder('./batch_files')

