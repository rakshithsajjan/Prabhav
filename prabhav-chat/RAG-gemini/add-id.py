import os
import json

def add_unique_ids(directory):
    # Get all JSON files in the directory
    json_files = [f for f in os.listdir(directory) if f.endswith('.json')]
    
    # Sort files to ensure consistent ordering
    json_files.sort()
    
    # Initialize the ID counter
    id_counter = 1
    
    for filename in json_files:
        file_path = os.path.join(directory, filename)
        
        # Read the JSON file
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        
        # Add the unique ID
        data['id'] = f'{id_counter:06d}'
        
        # Write the updated JSON back to the file
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
        
        print(f"Added ID {data['id']} to {filename}")
        
        # Increment the counter
        id_counter += 1

# Specify the directory containing the JSON files
directory = '/Users/rakshithsajjan/Desktop/Prabhav/prabhav-chat/RAG-gemini/cleandata'

# Run the function
add_unique_ids(directory)