import os
import json
import glob

# Define input and output directories
def combine_jsonl_files(input_dir, output_dir):
    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Define output file path
    output_file = os.path.join(output_dir, 'combined_data.jsonl')

    # Get all jsonl files in the input directory
    jsonl_files = glob.glob(os.path.join(input_dir, '*.jsonl'))

    # Combine all jsonl files
    with open(output_file, 'w') as outfile:
        for jsonl_file in jsonl_files:
            with open(jsonl_file, 'r') as infile:
                for line in infile:
                    outfile.write(line)

    print(f"All JSONL files have been combined into {output_file}")

# Example usage
#input_dir = '/Users/rakshithsajjan/Downloads/data1'
#output_dir = './cleandata'
#combine_jsonl_files(input_dir, output_dir)

import json
import os

def extract_and_rename_jsons(input_file, output_dir):
    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    with open(input_file, 'r') as file:
        for line in file:
            data = json.loads(line)
            # Extract the title and content
            content = json.loads(data['response']['body']['choices'][0]['message']['content'])
            title = content['title']

            # Create a new JSON object with only the content
            new_data = {'content': content}

            # Define the output file path, replacing spaces with underscores in the title
            output_file_path = os.path.join(output_dir, f"{title.replace(' ', '_')}.json")

            # Write the new JSON data to the file
            with open(output_file_path, 'w') as outfile:
                json.dump(new_data, outfile, indent=4)

            print(f"Exported {title} to {output_file_path}")


import os

def extract_and_rename_jsons1(input_file, output_dir):
    with open(input_file, 'r') as file:
        for line in file:
            data = json.loads(line)
            content = json.loads(data['response']['body']['choices'][0]['message']['content'])
            title = content['title']
            new_data = {'content': content}

            # Sanitize title to create a valid file path
            sanitized_title = title.replace(' ', '_').replace('/', '_')
            output_file_path = os.path.join(output_dir, f"{sanitized_title}.json")

            # Ensure the directory exists
            os.makedirs(os.path.dirname(output_file_path), exist_ok=True)

            with open(output_file_path, 'w') as outfile:
                json.dump(new_data, outfile, indent=4)

            print(f"Exported {title} to {output_file_path}")



# Example usage
input_file = '/Users/rakshithsajjan/Desktop/Prabhav/prabhav-chat/RAG/combined_data.jsonl'
output_dir = '/Users/rakshithsajjan/Desktop/Prabhav/prabhav-chat/RAG/cleandata'
extract_and_rename_jsons1(input_file, output_dir)