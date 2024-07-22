import openai
import os
import json
from openai import OpenAI
import pandas as pd
from IPython.display import Image, display

with open('cleaningprompt.txt', 'r') as f:
    base_prompt = f.read()

if not os.path.exists('json'):
    os.makedirs('json')



def clean(filename):
    response = client.chat.completions.create(
    model="gpt-4o-mini",
    temperature=0.1,
    # This is to enable JSON mode, making sure responses are valid json objects
    response_format={ 
        "type": "json_object"
    },
    messages=[
        {
            "role": "system",
            "content": base_prompt
        },
        {
            "role": "user",
            "content": filename
        }
    ],
    )

    return response.choices[0].message.content


def call():
    all_files = os.listdir('data')
    batch_size = 100
    
    for batch_start in range(0, len(all_files), batch_size):
        tasks = []
        batch_end = min(batch_start + batch_size, len(all_files))
        batch_files = all_files[batch_start:batch_end]
        
        for filename in batch_files:
            with open(os.path.join('data', filename), 'r') as file:
                file_content = file.read()
                
                task = {
                    "custom_id": f"task-{filename}",
                    "method": "POST",
                    "url": "/v1/chat/completions",
                    "body": {
                        "model": "gpt-4o-mini",
                        "temperature": 0.1,
                        "response_format": { 
                            "type": "json_object"
                        },
                        "messages": [
                            {
                                "role": "system",
                                "content": base_prompt
                            },
                            {
                                "role": "user",
                                "content": file_content
                            }
                        ],
                    }
                }
                
                tasks.append(task)

        file_name = f"clean-data-jsonl-{batch_start+1}-{batch_end}.jsonl"

        with open(file_name, 'w') as file:
            for obj in tasks:
                file.write(json.dumps(obj) + '\n')

        batch_file = client.files.create(
            file=open(file_name, "rb"),
            purpose="batch"
        )
        print(f"Batch file created: {batch_file}")

call()