import os

# Define the directory to search
data_folder = 'data'

# Define the keywords to search for
keywords = ['agriculture', 'farmer', 'farmers']

# Create a list to store matching file names
matching_files = []

# Walk through the directory and its subdirectories
for root, dirs, files in os.walk(data_folder):
    for file in files:
        if file.endswith('.md'):

                        # Open the file and check if any of the keywords are in the file contents
                        with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                            content = f.read()
                            if any(keyword in content for keyword in keywords):
                                matching_files.append(file)

# Write the matching file names to a new text file
with open('farmers.txt', 'w') as output_file:
    for file_name in matching_files:
        output_file.write(file_name + '\n')
# Create the farmers folder if it doesn't exist
if not os.path.exists('farmers'):
    os.makedirs('farmers')

# Copy matching files to the farmers folder
for file_name in matching_files:
    src_path = os.path.join(data_folder, file_name)
    dst_path = os.path.join('farmers', file_name)
    with open(src_path, 'r', encoding='utf-8') as src_file, open(dst_path, 'w', encoding='utf-8') as dst_file:
        dst_file.write(src_file.read())
