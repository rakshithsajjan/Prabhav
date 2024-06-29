import requests

# API Settings
url = "https://api.myscheme.gov.in/search/v4/schemes"
headers = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "en-US,en;q=0.9",
    "origin": "https://www.myscheme.gov.in",
    "priority": "u=1, i",
    "sec-ch-ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"", 
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    "x-api-key": "tYTy5eEhlu9rFjyxuCr7ra7ACp4dv1RH8gWuHTDc"  # Replace with your actual API key
}

# Pagination Variables
from_value = 0  
page_size = 100 
total_entries = 2283 

# Loop through pages to extract all slugs
for i in range(from_value, total_entries, page_size):
    querystring = {"lang":"en","q":"[]","keyword":"","sort":"","from": str(i), "size": str(page_size)}
    
    response = requests.get(url, headers=headers, params=querystring)

    if response.status_code == 200:
        data = response.json()
        
        # Extract and print slugs for the current page
        for item in data.get("data", {}).get("hits", {}).get("items", []):
            slug = item.get("fields", {}).get("slug")
            if slug:
                print(slug)
    else:
        print(f"Error fetching data: {response.status_code}")


# Print the size of the slug list
print(f"Total number of slugs: {total_entries}")

def export_slugs_to_file():
    with open("slugs.txt", "w") as file:
        for i in range(from_value, total_entries, page_size):
            querystring = {"lang":"en","q":"[]","keyword":"","sort":"","from": str(i), "size": str(page_size)}
            
            response = requests.get(url, headers=headers, params=querystring)

            if response.status_code == 200:
                data = response.json()
                
                # Extract and write slugs for the current page
                for item in data.get("data", {}).get("hits", {}).get("items", []):
                    slug = item.get("fields", {}).get("slug")
                    if slug:
                        file.write(slug + "\n")
            else:
                print(f"Error fetching data: {response.status_code}")

# Call the function to export slugs to file
export_slugs_to_file()
