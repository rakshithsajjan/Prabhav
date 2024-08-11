import json
from collections import Counter
import google.generativeai as genai

# Configure the Gemini API
import os
from dotenv import load_dotenv

# Specify the path to your .env file
env_path = os.path.join(os.path.dirname(__file__), '..', 'config', '.env')

# Load the .env file
load_dotenv(dotenv_path=env_path)

# Access the environment variables
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))

def load_tag_index(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

def search_schemes(query, tag_index, additional_tags):
    # Convert query to lowercase and split into words
    query_words = query.lower().split()
    
    # Combine query words with additional tags
    all_search_terms = query_words + additional_tags
    
    # Find matching tags
    matching_tags = [tag for tag in tag_index.keys() if any(word in tag.lower() for word in all_search_terms)]
    
    # Get schemes for matching tags
    matching_schemes = []
    for tag in matching_tags:
        matching_schemes.extend(tag_index[tag])
    
    # Count occurrences of each scheme
    scheme_counts = Counter(matching_schemes)
    
    # Sort schemes by relevance (number of matching tags)
    sorted_schemes = sorted(scheme_counts.items(), key=lambda x: x[1], reverse=True)
    
    return [scheme for scheme, count in sorted_schemes]

# Function to generate tags using Gemini API
def generate_tags_with_gemini(query):
    model = genai.GenerativeModel('gemini-1.5-pro')
    prompt = f"""
    Given the query: '{query}'
    
    1. Identify the language of the query.
    2. Translate the query to English if it's not already in English.
    3. Generate 50 relevant tags for government schemes based on this query.
    4. Include tags in both English and the original query language (if different).
    5. Consider various aspects such as:
       - Target beneficiaries (e.g., women, farmers, students)
       - Specific needs or goals (e.g., education, employment, healthcare)
       - Related government departments or initiatives
       - Relevant industries or sectors
    6. Provide only the tags, separated by commas, without numbering or additional text.
    
    Tags:
    """
    
    response = model.generate_content(prompt)
    generated_tags = response.text.strip().split(',')
    return [tag.strip().lower() for tag in generated_tags]

# Combined search function
def combined_search(query, tag_index):
    additional_tags = generate_tags_with_gemini(query)
    results = search_schemes(query, tag_index, additional_tags)
    return results, additional_tags

# Load the tag index
tag_index = load_tag_index('tag_index.json')

# Use the combined search function
user_query = "mai ek aurat hu, aur mujhai tailoring karna hai"
results, additional_tags = combined_search(user_query, tag_index)

print(f"Matching schemes: {results}")  
print(f"number of results: {len(results)}")
print(f"number of additional tags: {len(additional_tags)}")
print(f"\n\nAdditional tags generated: {additional_tags}")


