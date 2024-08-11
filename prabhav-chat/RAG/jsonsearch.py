import json
from collections import Counter
from openai import OpenAI

# Initialize the client
client = OpenAI(api_key='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')

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

# Function to generate tags using OpenAI API
def generate_tags_with_openai(query):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that generates relevant tags for government scheme queries. No # ."},
            {"role": "user", "content": f"Generate 50 relevant tags for the query: '{query}'\nTags:"}
        ],
        max_tokens=70,
        n=1,
        temperature=0.5,
    )
    
    generated_tags = response.choices[0].message.content.strip().split(',')
    return [tag.strip().lower() for tag in generated_tags]

# Combined search function
def combined_search(query, tag_index):
    additional_tags = generate_tags_with_openai(query)
    results = search_schemes(query, tag_index, additional_tags)
    return results, additional_tags

# Load the tag index
tag_index = load_tag_index('tag_index.json')

# Use the combined search function
user_query = "mai ek aurat hu, aur mujhai tailoring karna hai"
results, additional_tags = combined_search(user_query, tag_index)
print(f"Matching schemes: {results}")  
print(f" \n \n \n \n \n \n \n \n Additional tags generated: {additional_tags}")





