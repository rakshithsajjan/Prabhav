#1. got gemini embeddings (rakshith)

#2. use pinecone to retrieve using metadata filter
    # get all the tags
    # use that to query search with metadata filter, topk=100
    # then use those for similarity search

import os, json
import time
import logging
from pinecone.grpc import PineconeGRPC as Pinecone


load_dotenv()
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_INDEX_NAME = os.getenv("PINECONE_INDEX_NAME")
pc = Pinecone(api_key=PINECONE_API_KEY)
index = pc.Index(PINECONE_INDEX_NAME)


# index.query(
#     # vector=[0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1],
#     filter={
#         "genre": {"$eq": "documentary"},
#         "year": 2019
#     },
#     top_k=1,
#     include_metadata=True
# )

# Returns:
# {'matches': [{'id': 'B',
#               'metadata': {'genre': 'documentary', 'year': 2019.0},
#               'score': 0.0800000429,
#               'values': []}],
#  'namespace': ''}


# # get all the tags
# def get_unique_tags(directory):
#     unique_tags = []
#     for filename in os.listdir(directory):
#         if filename.endswith(".json"):
#             with open(os.path.join(DIRECTORY, filename)) as f:
#                 data = json.load(f)
#                 tags = data.get('content', {}).get('tags', [])
#                 for tag in tags:
#                     if tag not in unique_tags:
#                         with open("unique_tags.txt", "a") as file:
#                             file.write(f"{tag}, ")
#                         unique_tags.append(tag)
#                     else:
#                         print(f"skipped duplicate tag: {tag}")
#     # return unique tags
#     return unique_tags

# DIRECTORY="../../../data/cleandata/"
# unique_tags = get_unique_tags(DIRECTORY)

# print(f"total unique tags: {len(unique_tags)}")
# print(f"unique tags = {unique_tags[:10]}")