import json

def check_custom_ids(jsonl_file_path):
    custom_ids = set()
    duplicates = []

    with open(jsonl_file_path, 'r') as file:
        for line_number, line in enumerate(file, 1):
            try:
                data = json.loads(line)
                custom_id = data.get('custom_id')
                
                if custom_id:
                    if custom_id in custom_ids:
                        duplicates.append((custom_id, line_number))
                    else:
                        custom_ids.add(custom_id)
                else:
                    print(f"Warning: No custom_id found in line {line_number}")
            
            except json.JSONDecodeError:
                print(f"Error: Invalid JSON in line {line_number}")

    if duplicates:
        print("Duplicate custom_ids found:")
        for custom_id, line_number in duplicates:
            print(f"Custom ID '{custom_id}' repeated at line {line_number}")
    else:
        print("No duplicate custom_ids found.")

    return len(duplicates) == 0

# Example usage:
# is_valid = check_custom_ids('path/to/your/jsonl/file.jsonl')
# print(f"Are all custom_ids unique? {is_valid}")
check_custom_ids('clean.jsonl')