import requests
import os
import time

base_url = "https://www.myscheme.gov.in/schemes/"
payload = ""
headers = {"Authorization": "Bearer jina_d3cc9f76b42941a38b23f84fb640ee30UsXgsFovJmCS3g8LO_o-7cWsT7uq"}

# Create data directory if it doesn't exist
if not os.path.exists("data"):
    os.makedirs("data")

with open("slugs.txt", "r") as file:
    slugs = file.readlines()

for slug in slugs:
    slug = slug.strip()
    url = base_url + slug
    response = requests.request("GET", url, data=payload, headers=headers)
    
    # Write the response to a markdown file
    with open(f"data/{slug}.md", "w") as md_file:
        md_file.write(response.text)
    
    # Wait for 1 second before the next request
    time.sleep(1)
