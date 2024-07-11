import requests
import os
import time

base_url = "https://r.jina.ai/https://www.myscheme.gov.in/schemes/"
payload = ""
headers = {"Authorization": "Bearer jina_69a74127c2d8499c93431a587e3b3ba7rQQGGj9wO-OcwMfZLRwRB_p5ARka"}

#second bearer key = jina_fe0c87476f234840bef119840cf601c0XtlCq4Mn3s1TgOzXTIiiOn2W9EpO
#third bearer key = jina_e2b77ab9e0e242caa4d7239710226a031FNLG9ZgzuYE7NXX0mKWFoc2-RcN
#

# Create data directory if it doesn't exist


if not os.path.exists("data"):
    os.makedirs("data")

with open("slugs.txt", "r") as file:
    slugs = file.readlines()

slugs = [slug.strip() for slug in slugs]  # Strip each slug in the list

counter = 0
start_time = time.time()
for slug in slugs[751:1050]:  # Limit to first 150 slugs
    url = base_url + slug
    response = requests.request("GET", url, data=payload, headers=headers)
    with open(f"data/{slug}.md", "w") as md_file:
        md_file.write(response.text)
    
    counter += 1
    if counter % 5 == 0:
        percentage_done = (counter / 150) * 300
        elapsed_time = time.time() - start_time
        estimated_total_time = (elapsed_time / counter) * 300
        estimated_remaining_time = estimated_total_time - elapsed_time
        print(f"Processed {counter} slugs, percentage done = {percentage_done:.2f}%, time elapsed = {elapsed_time:.2f} seconds, estimated remaining time = {estimated_remaining_time:.2f} seconds")
        
    