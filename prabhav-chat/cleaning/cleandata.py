import openai
import os
import json
from openai import OpenAI
import pandas as pd
from IPython.display import Image, display
client = OpenAI()


with open('cleaningprompt.txt', 'r') as f:
    base_prompt = f.read()

if not os.path.exists('json'):
    os.makedirs('json')

counter = 0
with open('donejson.txt', 'w') as done_file:
    for filename in os.listdir('data')[:10]:
        if filename.endswith('.md'):
            with open(os.path.join('data', filename), 'r') as file:
                file_content = file.read()
                prompt = base_prompt + file_content
                response = openai.ChatCompletion.create(
                    model="gpt-4o-mini",
                    messages=[{"role": "user", "content": prompt}]
                )
                with open(os.path.join('json', f"{filename}.json"), 'w') as json_file:
                    json_file.write(response['choices'][0]['message']['content'])
                done_file.write(filename + '\n')

            
                print(f"Iteration done: {filename}")
                counter = counter + 1
                print(counter)
