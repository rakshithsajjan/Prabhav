
import tiktoken

def count_tokens(text):
    encoding = tiktoken.get_encoding("gpt2")
    tokens = encoding.encode(text)
    return len(tokens)
import json

def read_jsonl_file(file_path):
    with open(file_path, 'r') as file:
        return [json.loads(line) for line in file]




import os

def read_all_data_files():
    data_folder = 'data'
    rr = ""
    for filename in os.listdir(data_folder):
        if filename.endswith('.md'):  # Assuming the files are markdown files
            file_path = os.path.join(data_folder, filename)
            with open(file_path, 'r', encoding='utf-8') as file:
                rr += file.read() + "\n\n"  # Add a newline between files for separation
    return rr

rr = read_all_data_files()

r1r = read_jsonl_file('clean-data-jsonl.jsonl')
r = '''import requests



#hello
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
    with open("slugs1.txt", "w") as file:
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
'''
r= ''' Given the provided JSON schema and the Markdown input, extract the relevant scheme information and output it as a valid JSON object conforming to the schema. Ensure to accurately capture and structure the data, including titles, lists, URLs, and other relevant details.### JSON Schema

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Scheme Information",
  "description": "Schema for representing details about a government scheme",
  "type": "object",
  "properties": {
    "title": {
      "type": "string",
      "description": "Official title of the scheme"
    },
    "state": {
      "type": "string",
      "description": "State where the scheme is applicable"
    },
    "department": {
      "type": "string",
      "description": "Government department managing the scheme"
    },
    "type": {
      "type": "string",
      "description": "Type of scheme (e.g., Subsidy, Grant, Loan)"
    },
    "beneficiary": {
      "type": "string",
      "description": "Target beneficiary of the scheme"
    },
    "details": {
      "type": "string",
      "description": "Detailed description of the scheme"
    },
    "benefits": {
      "type": "array",
      "description": "List of benefits offered by the scheme",
      "items": {
        "type": "string"
      }
    },
    "eligibility": {
      "type": "array",
      "description": "Eligibility criteria for the scheme",
      "items": {
        "type": "string"
      }
    },
    "exclusions": {
      "type": "array",
      "description": "Exclusions or restrictions of the scheme",
      "items": {
        "type": "string"
      }
    },
    "application_process": {
      "type": "string",
      "description": "Mode of application (e.g., Online, Offline)"
    },
    "documents_required": {
      "type": "array",
      "description": "List of documents required for application",
      "items": {
        "type": "string"
      }
    },
    "faqs": {
      "type": "array",
      "description": "Frequently asked questions about the scheme",
      "items": {
        "type": "object",
        "properties": {
          "question": {
            "type": "string"
          },
          "answer": {
            "type": "string"
          }
        },
        "required": [
          "question",
          "answer"
        ]
      }
    },
    "sources": {
      "type": "array",
      "description": "Links to official sources and documents",
      "items": {
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "description": "Type of source (e.g., Guidelines, Application Form)"
          },
          "url": {
            "type": "string",
            "format": "uri"
          }
        },
        "required": [
          "type",
          "url"
        ]
      }
    },
    "tags": {
      "type": "array",
      "description": "Relevant tags for categorizing the scheme",
      "items": {
        "type": "string"
      }
    }
  },
  "required": [
    "title",
    "state",
    "department",
    "type",
    "beneficiary",
    "details",
    "benefits",
    "eligibility",
    "application_process",
    "documents_required",
    "tags"
  ]
}

input
"
Title: 40% Subsidy On Hank Yarn, Dyes & Chemicals Scheme

URL Source: https://www.myscheme.gov.in/schemes/40shydcs

Markdown Content:
40% Subsidy On Hank Yarn, Dyes & Chemicals Scheme
===============


### Are you sure you want to sign out?

CancelSign Out

[![Image 1: Ministry of Electronics and Information Technology](https://cdn.myscheme.in/images/logos/emblem-black.svg)](https://www.myscheme.gov.in/)

![Image 2: myScheme](https://cdn.myscheme.in/images/logos/myscheme-logo-black.svg)
==================================================================================

[![Image 3](blob:https://www.myscheme.gov.in/7029bfa5283c1934d72d4efe1c626373)![Image 4: Digital India Corporation](https://cdn.myscheme.in/images/logos/digital-india-black.svg)](https://www.digitalindia.gov.in/)

*   ![Image 5](blob:https://www.myscheme.gov.in/39e3356370f513e3664ceae4ebfc3a5a)![Image 6: Change language](blob:https://www.myscheme.gov.in/b9a31d3949b1882a09ed2f8508d538f3)

    Eng


[![Image 7: Ministry of Electronics and Information Technology](https://cdn.myscheme.in/images/logos/emblem-black.svg)](https://www.myscheme.gov.in/)

![Image 8: myScheme](https://cdn.myscheme.in/images/logos/myscheme-logo-black.svg)

[![Image 9](blob:https://www.myscheme.gov.in/04e0786ebe0ffe2b3244c2451b75b80f)![Image 10: Digital India Corporation](https://cdn.myscheme.in/images/logos/digital-india-black.svg)](https://www.digitalindia.gov.in/)

![Image 11](blob:https://www.myscheme.gov.in/39e3356370f513e3664ceae4ebfc3a5a)![Image 12: Change language](https://cdn.myscheme.in/images/icons/language.svg)English/हिंदी

Theme

*   Sign In

Back

*   Details
*   Benefits
*   Eligibility
*   Exclusions
*   Application Process
*   Documents Required
*   Frequently Asked Questions
*   Sources And References
*   Feedback

### Something went wrong. Please try again later.

Ok

###

### You need to sign in before applying for schemes

CancelSign In

### Something went wrong. Please try again later.

Ok

###

It seems you have already initiated your application earlier.To know more please visit

Cancel

### Apply Now

### Check Eligibility

Andhra Pradesh
--------------

40% Subsidy On Hank Yarn, Dyes & Chemicals Scheme
=================================================

Handloom

Subsidy

Weaver

[### Details](https://www.myscheme.gov.in/schemes/40shydcs#details)

The "40% subsidy on Hank Yarn, Dyes & Chemicals Scheme" is a Subsidy Scheme by the Department of Handlooms & Textiles, Government of Andhra Pradesh. The entire assistance under the scheme will be in the form of Grant from the State Government. The scheme is operative from 29th April 2011. The subsidy will be available only on purchases / procurements from NHDC & APCO. The amount sanctioned will be credited directly to the members bank account of the concerned primary weavers cooperative societies.

[### Benefits](https://www.myscheme.gov.in/schemes/40shydcs#benefits)

1.  40% subsidy on the purchases / procurements of Hank Yarn, Dyes & Chemicals from NHDC & APCO.
2.  The 75% amount will be credited directly to the members bank account of the concerned primary weavers cooperative societies as production bonus basing on the wages earned by them.
3.  The remaining 25% amount may be utilized by the societies for giving rebate on sales or any other production related purpose.

[### Eligibility](https://www.myscheme.gov.in/schemes/40shydcs#eligibility)

1.  The subsidy will be available only on purchase / procurement of yarn from NHDC, Yarn Deports sanctioned by NHDC and APCO for self-consumption of Handloom Weaver Cooperative Societies for providing work to weaver members.
2.  The subsidy will be allowed only on the Hank yarn purchased from the APCO & NHDC and its depots and utilized for the production on Societies, account during the quarter.
3.  The claims for subsidy shall be submitted by the Weavers Cooperative Societies in the prescribed proforma on quarterly basis during the financial year with in 15 days from the end of the respective quarter.
4.  The claims for subsidy in complete shape should reach Head Office with in 30 days from the end of the Quarter.

﻿

﻿

**NOTE 1:** The Weavers Coop Societies shall NOT claim any subsidy on the Yarn, Dyes and Chemicals purchased from private yarn dealers, Mills etc.

**NOTE 2:** The Weavers Coop. Societies should NOT claim any subsidy on Yarn, Dyes & Chemicals even if purchased from APCO or NHDC, but not utilized for production of cloth by way of issue of yarn and sold to non-members.

﻿

﻿

[### Exclusions](https://www.myscheme.gov.in/schemes/40shydcs#exclusions)

1.  The Weavers Cooperative Societies shall not claim any subsidy on the Yarn, Dyes and Chemicals purchased from private yarn dealers, Mills etc.
2.  The Weavers Coop. Societies should not claim any subsidy on Yarn, Dyes & Chemicals even if purchased from APCO or NHDC, but not utilized for production of cloth by way of issue of yarn and sold to non-members.

[### Application Process](https://www.myscheme.gov.in/schemes/40shydcs#application-process)

Offline

> **Application:**

**Step 1:** The claims for subsidy shall be submitted by the Weavers Cooperative Societies to the Assistant Director (H&T) in the prescribed proforma on quarterly basis during the financial year within 15 days from the end of the respective quarter.

**Step 2:** The AD(H&T) after scrutiny shall recommend the claims with in next 15 days.

**Step 3:** All claims in complete shape should reach Head Office with in 30 days from the end of the Quarter.

﻿

**NOTE:** _Appropriate cut will be imposed on bleated claims._

﻿

> **Disbursal of the Subsidy:**

1.  The amount sanctioned as 40% Yarn subsidy, 75% amount will be credited directly to the members bank account of the concerned primary Weavers Cooperative Societies as production bonus basing on the wages earned by them.
2.  The societies may utilize the remaining 25% amount for giving rebate on sales or any other production related purpose with effect from 1st Dec 2016.

[### Documents Required](https://www.myscheme.gov.in/schemes/40shydcs#documents-required)

1.  Certification that subsidy has been claimed only on the Hank Yarn and Dyes & Chemicals supplied to the members and utilized for production on Societies account from out of the Yarn and Dyes & Chemicals purchased from the NHDC and APCO.
2.  Photocopies of invoices/receipts of hank yarn and Dyes & Chemicals purchased/procured from NHDC, its depots and APCO.
3.  The abstract duly attested by the concerned Assistant Director (H&T).
4.  Registers, Stock Register, Cash Book and other relevant records as required by the Assistant Director (H&T).

[### Frequently Asked Questions](https://www.myscheme.gov.in/schemes/40shydcs#faqs)

Which Department Manages This Scheme?

This scheme is managed by the Department of Handlooms & Textiles, Government of Andhra Pradesh.

Is This Scheme State Sponsored Or Centrally Sponsored?

This scheme is a 100% State Sponsored Scheme.

Where Can I Find The Link To The Original Scheme Guidelines?

The Scheme Guidelines can be found at this link - https://www.aphandtex.gov.in/open\_record.php?ID=136

Where Can I Find The Link To The Amended Scheme Guidelines?

The Scheme Guidelines can be found at this link - https://handlooms.ap.gov.in/documents/G\_O\_55%20Yarn\_subsidy.PDF

What Is The Full Form Of NHDC?

The Full Form of NHDC is "National Handloom Development Corporation Limited".

What Is The Address Of NHDC?

The address of NHDC is: Vikas Deep, 22, Station Road, Chitwapur Bhuiyan, Udaiganj, Husainganj, Lucknow, Uttar Pradesh - 226 001.

What Is The Full Form Of APCO?

The Full Form of APCO is "Andhra Pradesh State Handloom Weavers Cooperative Society".

Does This Scheme Accept Online Applications?

No, this scheme only accepts offline applications. The claims for subsidy shall be submitted by the Weavers Cooperative Societies to the Assistant Director (H&T) in the prescribed proforma.

What Is The URL Of The Website Of Department Of Handlooms & Textiles, Government Of Andhra Pradesh.?

The URL of the website of Department of Handlooms & Textiles is https://www.aphandtex.gov.in/home.php.

Is There Any Application Fee?

No. The entire application process is completely free of cost.

Is There A Percentage Of Slots Reserved For Female Applicants?

No, there is no reservation of slots based on the gender of the applicant.

For What Purposes Can The Amount Of Subsidy Be Utilized?

The amount of Subsidy should be utilized for: 1. as production bonus basing on the wages earned by the members of the concerned primary Weavers Cooperative Societies. 2. rebate on sales or any other production related purpose.

What Percentage Of The Amount Of Subsidy Can Be Utilized As Production Bonus Basing On The Wages Earned By The Members?

75% of the amount of subsidy can be utilized as production bonus basing on the wages earned by the members of the concerned primary Weavers Cooperative Societies.

What Percentage Of The Amount Of Subsidy Can Be Utilized As Rebate On Sales Or Any Other Production Related Purpose?

25% of the amount of subsidy can be utilized as rebate on sales or any other production related purpose with effect from 1st Dec 2016.

What Is The Full Form Of AD (H&T)?

The Full Form of AD (H&T) is Assistant Director (Department of Handlooms & Textiles).

Is There A Deadline For The Submission Of The Claims For Subsidy?

Yes, the claims for subsidy shall be submitted by the Weavers Cooperative Societies to the Assistant Director (H&T) in the prescribed proforma on quarterly basis during the financial year within 15 days from the end of the respective quarter.

Is There A Deadline For The AD(H&T) For Recommending The Claims?

Yes, the AD(H&T) after scrutiny shall recommend the claims with in next 15 days.

What Shall Be The Case If The Claims Are Found To Be Bleated?

Appropriate cut will be imposed on bleated claims.

Since When Is This Scheme Under Operation?

The scheme is operative from 29th April 2011.

Can The Weavers Coop Societies Claim Any Subsidy On The Yarn Purchased From Private Yarn Dealers?

No, the Weavers Coop Societies shall NOT claim any subsidy on the Yarn, Dyes and Chemicals purchased from private yarn dealers, Mills etc.

By When Should The Claim For Subsidy Reach Head Office?

The claims for subsidy in complete shape should reach Head Office with in 30 days from the end of the Quarter.

[### Sources And References](https://www.myscheme.gov.in/schemes/40shydcs#sources)

[Guidelines](https://www.aphandtex.gov.in/open_record.php?ID=136)

[Amendment (40% Subsidy)](https://handlooms.ap.gov.in/documents/G_O_55%20Yarn_subsidy.PDF)

Ok

Was this helpful?

#### News and Updates

No new news and updates available

#### Share

### Something went wrong. Please try again later.

Ok

###

### You need to sign in before applying for schemes

CancelSign In

### Something went wrong. Please try again later.

Ok

###

It seems you have already initiated your application earlier.To know more please visit

Cancel

### Apply Now

### Check Eligibility

Andhra Pradesh
--------------

40% Subsidy On Hank Yarn, Dyes & Chemicals Scheme
=================================================

Handloom

Subsidy

Weaver

Details

Benefits

Eligibility

Exclusions

Application Process

Documents Required

Frequently Asked Questions

The "40% subsidy on Hank Yarn, Dyes & Chemicals Scheme" is a Subsidy Scheme by the Department of Handlooms & Textiles, Government of Andhra Pradesh. The entire assistance under the scheme will be in the form of Grant from the State Government. The scheme is operative from 29th April 2011. The subsidy will be available only on purchases / procurements from NHDC & APCO. The amount sanctioned will be credited directly to the members bank account of the concerned primary weavers cooperative societies.

Ok

Was this helpful?

#### Share

#### News and Updates

No new news and updates available

©2024

[![Image 13: myScheme](blob:https://www.myscheme.gov.in/b9a31d3949b1882a09ed2f8508d538f3)](https://www.myscheme.gov.in/)

Powered by![Image 14](blob:https://www.myscheme.gov.in/a01e597e35ed1eeaefa52c5d0c5fe71b)![Image 15: Digital India](blob:https://www.myscheme.gov.in/b9a31d3949b1882a09ed2f8508d538f3)

Digital India Corporation(DIC)Ministry of Electronics & IT (MeitY)Government of India®

Quick Links
-----------

*   [About Us](https://www.myscheme.gov.in/about)
*   [Contact Us](https://www.myscheme.gov.in/contact)
*   [Screen Reader](https://www.myscheme.gov.in/screen-reader)
*   [Accessibility Statement](https://www.myscheme.gov.in/accessibility-statement)
*   [Frequently Asked Questions](https://www.myscheme.gov.in/faqs)
*   [Disclaimer](https://www.myscheme.gov.in/disclaimer)
*   [Terms & Conditions](https://www.myscheme.gov.in/terms-conditions)

Useful Links
------------

*   ![Image 16: di](blob:https://www.myscheme.gov.in/b9a31d3949b1882a09ed2f8508d538f3)

*   ![Image 17: digilocker](blob:https://www.myscheme.gov.in/b9a31d3949b1882a09ed2f8508d538f3)

*   ![Image 18: umang](blob:https://www.myscheme.gov.in/b9a31d3949b1882a09ed2f8508d538f3)

*   ![Image 19: indiaGov](blob:https://www.myscheme.gov.in/b9a31d3949b1882a09ed2f8508d538f3)

*   ![Image 20: myGov](blob:https://www.myscheme.gov.in/b9a31d3949b1882a09ed2f8508d538f3)

*   ![Image 21: dataGov](blob:https://www.myscheme.gov.in/b9a31d3949b1882a09ed2f8508d538f3)

*   ![Image 22: igod](blob:https://www.myscheme.gov.in/b9a31d3949b1882a09ed2f8508d538f3)


Get in touch
------------

4th Floor, NeGD, Electronics Niketan, 6 CGO Complex, Lodhi Road, New Delhi - 110003, India

support-myscheme\[at\]digitalindia\[dot\]gov\[dot\]in

(011) 24303714

Last Updated On : 09/07/2024 | v-2.1.8

"

json
Copy code
{
  "title": "40% Subsidy On Hank Yarn, Dyes & Chemicals Scheme",
  "state": "Andhra Pradesh",
  "department": "Department of Handlooms & Textiles",
  "type": "Subsidy",
  "beneficiary": "Weaver",
  "details": "The '40% subsidy on Hank Yarn, Dyes & Chemicals Scheme' is a Subsidy Scheme by the Department of Handlooms & Textiles, Government of Andhra Pradesh. The entire assistance under the scheme will be in the form of Grant from the State Government. The scheme is operative from 29th April 2011. The subsidy will be available only on purchases / procurements from NHDC & APCO. The amount sanctioned will be credited directly to the members bank account of the concerned primary weavers cooperative societies.",
  "benefits": [
    "40% subsidy on the purchases / procurements of Hank Yarn, Dyes & Chemicals from NHDC & APCO.",
    "The 75% amount will be credited directly to the members bank account of the concerned primary weavers cooperative societies as production bonus basing on the wages earned by them.",
    "The remaining 25% amount may be utilized by the societies for giving rebate on sales or any other production related purpose."
  ],
  "eligibility": [
    "The subsidy will be available only on purchase / procurement of yarn from NHDC, Yarn Deports sanctioned by NHDC and APCO for self-consumption of Handloom Weaver Cooperative Societies for providing work to weaver members.",
    "The subsidy will be allowed only on the Hank yarn purchased from the APCO & NHDC and its depots and utilized for the production on Societies, account during the quarter.",
    "The claims for subsidy shall be submitted by the Weavers Cooperative Societies in the prescribed proforma on quarterly basis during the financial year with in 15 days from the end of the respective quarter.",
    "The claims for subsidy in complete shape should reach Head Office with in 30 days from the end of the Quarter."
  ],
  "exclusions": [
    "The Weavers Cooperative Societies shall not claim any subsidy on the Yarn, Dyes and Chemicals purchased from private yarn dealers, Mills etc.",
    "The Weavers Coop. Societies should not claim any subsidy on Yarn, Dyes & Chemicals even if purchased from APCO or NHDC, but not utilized for production of cloth by way of issue of yarn and sold to non-members."
  ],
  "application_process": "Offline",
  "documents_required": [
    "Certification that subsidy has been claimed only on the Hank Yarn and Dyes & Chemicals supplied to the members and utilized for production on Societies account from out of the Yarn and Dyes & Chemicals purchased from the NHDC and APCO.",
    "Photocopies of invoices/receipts of hank yarn and Dyes & Chemicals purchased/procured from NHDC, its depots and APCO.",
    "The abstract duly attested by the concerned Assistant Director (H&T).",
    "Registers, Stock Register, Cash Book and other relevant records as required by the Assistant Director (H&T)."
  ],
  "faqs": [
    {
      "question": "Which Department Manages This Scheme?",
      "answer": "This scheme is managed by the Department of Handlooms & Textiles, Government of Andhra Pradesh."
    },
    {
      "question": "Is This Scheme State Sponsored Or Centrally Sponsored?",
      "answer": "This scheme is a 100% State Sponsored Scheme."
    },
    {
      "question": "Where Can I Find The Link To The Original Scheme Guidelines?",
      "answer": "The Scheme Guidelines can be found at this link - https://www.aphandtex.gov.in/open_record.php?ID=136"
    },
    {
      "question": "Where Can I Find The Link To The Amended Scheme Guidelines?",
      "answer": "The Scheme Guidelines can be found at this link - https://handlooms.ap.gov.in/documents/G_O_55%20Yarn_subsidy.PDF"
    },
    {
      "question": "What Is The Full Form Of NHDC?",
      "answer": "The Full Form of NHDC is 'National Handloom Development Corporation Limited'."
    },
    {
      "question": "What Is The Address Of NHDC?",
      "answer": "The address of NHDC is: Vikas Deep, 22, Station Road, Chitwapur Bhuiyan, Udaiganj, Husainganj, Lucknow, Uttar Pradesh - 226 001."
    },
    {
      "question": "What Is The Full Form Of APCO?",
      "answer": "The Full Form of APCO is 'Andhra Pradesh State Handloom Weavers Cooperative Society'."
    },
    {
      "question": "Does This Scheme Accept Online Applications?",
      "answer": "No, this scheme only accepts offline applications. The claims for subsidy shall be submitted by the Weavers Cooperative Societies to the Assistant Director (H&T) in the prescribed proforma."
    },
    {
      "question": "What Is The URL Of The Website Of Department Of Handlooms & Textiles, Government Of Andhra Pradesh.?",
      "answer": "The URL of the website of Department of Handlooms & Textiles is https://www.aphandtex.gov.in/home.php."
    },
    {
      "question": "Is There Any Application Fee?",
      "answer": "No. The entire application process is completely free of cost."
    },
    {
      "question": "Is There A Percentage Of Slots Reserved For Female Applicants?",
      "answer": "No, there is no reservation of slots based on the gender of the applicant."
    },
    {
      "question": "For What Purposes Can The Amount Of Subsidy Be Utilized?",
      "answer": "The amount of Subsidy should be utilized for: 1. as production bonus basing on the wages earned by the members of the concerned primary Weavers Cooperative Societies. 2. rebate on sales or any other production related purpose."
    },
    {
      "question": "What Percentage Of The Amount Of Subsidy Can Be Utilized As Production Bonus Basing On The Wages Earned By The Members?",
      "answer": "75% of the amount of subsidy can be utilized as production bonus basing on the wages earned by the members of the concerned primary Weavers Cooperative Societies."
    },
    {
      "question": "What Percentage Of The Amount Of Subsidy Can Be Utilized As Rebate On Sales Or Any Other Production Related Purpose?",
      "answer": "25% of the amount of subsidy can be utilized as rebate on sales or any other production related purpose with effect from 1st Dec 2016."
    },
    {
      "question": "What Is The Full Form Of AD (H&T)?",
      "answer": "The Full Form of AD (H&T) is Assistant Director (Department of Handlooms & Textiles)."
    },
    {
      "question": "Is There A Deadline For The Submission Of The Claims For Subsidy?",
      "answer": "Yes, the claims for subsidy shall be submitted by the Weavers Cooperative Societies to the Assistant Director (H&T) in the prescribed proforma on quarterly basis during the financial year within 15 days from the end of the respective quarter."
    },
    {
      "question": "Is There A Deadline For The AD(H&T) For Recommending The Claims?",
      "answer": "Yes, the AD(H&T) after scrutiny shall recommend the claims with in next 15 days."
    },
    {
      "question": "What Shall Be The Case If The Claims Are Found To Be Bleated?",
      "answer": "Appropriate cut will be imposed on bleated claims."
    },
    {
      "question": "Since When Is This Scheme Under Operation?",
      "answer": "The scheme is operative from 29th April 2011."
    },
    {
      "question": "Can The Weavers Coop Societies Claim Any Subsidy On The Yarn Purchased From Private Yarn Dealers?",
      "answer": "No, the Weavers Coop Societies shall NOT claim any subsidy on the Yarn, Dyes and Chemicals purchased from private yarn dealers, Mills etc."
    },
    {
      "question": "By When Should The Claim For Subsidy Reach Head Office?",
      "answer": "The claims for subsidy in complete shape should reach Head Office with in 30 days from the end of the Quarter."
    }
  ],
  "sources": [
    {
      "type": "Guidelines",
      "url": "https://www.aphandtex.gov.in/open_record.php?ID=136"
    },
    {
      "type": "Amendment (40% Subsidy)",
      "url": "https://handlooms.ap.gov.in/documents/G_O_55%20Yarn_subsidy.PDF"
    }
  ],
  "tags": [
    "Handloom",
    "Subsidy",
    "Weaver"
  ]
}'''
print(count_tokens(rr))

import os

def count_files_in_data_folder():
    data_folder = 'data'  # This is correct as per the followup instruction
    file_count = len([name for name in os.listdir(data_folder) if os.path.isfile(os.path.join(data_folder, name))])
    print(f"Number of files in the data folder: {file_count}")

#count_files_in_data_folder()

def find_missing_files():
    data_folder = 'data'
    slugs_file = 'slugs.txt'
    
    # Read slugs from slugs.txt
    with open(slugs_file, 'r') as f:
        slugs = set(line.strip() for line in f)
    
    # Get existing files in data folder
    existing_files = set(os.path.splitext(name)[0] for name in os.listdir(data_folder) if os.path.isfile(os.path.join(data_folder, name)) and name.endswith('.md'))
    
    # Find missing files
    missing_files = slugs - existing_files
    
    print(f"Number of missing files: {len(missing_files)}")
    print("Missing files:")
    for file in sorted(missing_files):
        print(file)

#find_missing_files()

def find_repeating_slugs():
    slugs_file = 'slugs.txt'
    
    # Read slugs from slugs.txt
    with open(slugs_file, 'r') as f:
        slugs = [line.strip() for line in f]
    
    # Count occurrences of each slug
    slug_counts = {}
    for slug in slugs:
        if slug in slug_counts:
            slug_counts[slug] += 1
        else:
            slug_counts[slug] = 1
    
    # Find repeating slugs
    repeating_slugs = {slug: count for slug, count in slug_counts.items() if count > 1}
    
    print(f"Number of repeating slugs: {len(repeating_slugs)}")
    if repeating_slugs:
        print("Repeating slugs and their counts:")
        for slug, count in repeating_slugs.items():
            print(f"{slug}: {count}")
    else:
        print("No repeating slugs found.")

#find_repeating_slugs()
