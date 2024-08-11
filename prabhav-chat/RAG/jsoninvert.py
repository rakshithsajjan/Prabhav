import json
import os
from collections import defaultdict

def create_tag_index(cleandata_dir):
    tag_index = defaultdict(list)
    all_tags = set()
    for filename in os.listdir(cleandata_dir):
        if filename.endswith('.json'):
            file_path = os.path.join(cleandata_dir, filename)
            with open(file_path, 'r') as f:
                data = json.load(f)
                tags = data['content'].get('tags', [])
                for tag in tags:
                    tag_lower = tag.lower()
                    tag_index[tag_lower].append(filename)
                    all_tags.add(tag_lower)
    return tag_index, list(all_tags)

cleandata_dir = '/Users/rakshithsajjan/Desktop/Prabhav/prabhav-chat/RAG/cleandata'
tag_index, all_tags = create_tag_index(cleandata_dir)

# Define the output file paths
tag_index_file = '/Users/rakshithsajjan/Desktop/Prabhav/prabhav-chat/RAG/tag_index.json'
all_tags_file = '/Users/rakshithsajjan/Desktop/Prabhav/prabhav-chat/RAG/all_tags.json'

# Write the tag index to a JSON file
with open(tag_index_file, 'w') as f:
    json.dump(tag_index, f, indent=4)

# Write all tags to a JSON file
with open(all_tags_file, 'w') as f:
    json.dump(all_tags, f, indent=4)

print(f"Tag index has been written to {tag_index_file}")
print(f"All tags have been written to {all_tags_file}")
