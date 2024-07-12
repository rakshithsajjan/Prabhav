import google.generativeai as genai
import os

genai.configure(api_key="")

# Using `response_mime_type` requires one of the Gemini 1.5 Pro or 1.5 Flash models
model = genai.GenerativeModel('gemini-1.5-flash',
                              # Set the `response_mime_type` to output JSON
                              generation_config={"response_mime_type": "application/json"})

with open('cleaningprompt.txt', 'r') as f:
    base_prompt = f.read()

if not os.path.exists('json'):
    os.makedirs('json')


with open('donejson.txt', 'w') as done_file:
    for filename in os.listdir('data')[:10]:
        if filename.endswith('.md'):
            with open(os.path.join('data', filename), 'r') as file:
                file_content = file.read()
                prompt = base_prompt + file_content
                response = model.generate_content(prompt)
                with open(os.path.join('json', f"{filename}.json"), 'w') as json_file:
                    json_file.write(response.text)
                done_file.write(filename + '\n')
