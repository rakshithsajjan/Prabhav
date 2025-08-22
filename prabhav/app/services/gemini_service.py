# import os
# import json
# import time
# import logging
# from dotenv import load_dotenv
# from pinecone.grpc import PineconeGRPC as Pinecone
# import google.generativeai as genai

# load_dotenv()
# PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
# PINECONE_INDEX_NAME = os.getenv("PINECONE_INDEX_NAME")
# pc = Pinecone(api_key=PINECONE_API_KEY)
# index = pc.Index(PINECONE_INDEX_NAME)

# GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
# genai.configure(api_key=GEMINI_API_KEY)


# # response = model.generate_content("Write a story about an AI and magic")
# # print(index.describe_index_stats())


# def generate_response(message_body):  # , wa_id, name):
#     # get tags with gemini api of message_body
#     TAGS_PROMPT = f"""
#         you're a tag generating assistant. you're given examples of data in json format with existing tags as example.
#         Learn from it and you'll be given a new user query. Brainstorm and only output a list of tags.
#     """

#     # get gemini embeddings of message_body
#     result = genai.embed_content(
#         model="models/text-embedding-004",
#         content=message_body,
#         task_type="retrieval_document",
#         title="Embedding of single string")

#     # embedding
#     embedding = result['embedding']
#     # search top50
#     res = index.query(
#         vector=embedding,
#         # filter={
#         #     "genre": {"$eq": "documentary"},
#         #     "year": 2019
#         # },
#         top_k=50,
#         # include_metadata=True
#     )
#     print(res)
#     # out of them, do a similarity search
#     # add full context to prompt & get gemini response
#     # gemini_model = genai.GenerativeModel('gemini-1.5-flash')

#     # return new_message


# generate_response("what is margadarshan scheme?")


# # Returns:
# # {'matches': [{'id': 'B',
# #               'metadata': {'genre': 'documentary', 'year': 2019.0},
# #               'score': 0.0800000429,
# #               'values': []}],
# #  'namespace': ''}


# # # get all the tags
# # def get_unique_tags(directory):
# #     unique_tags = []
# #     for filename in os.listdir(directory):
# #         if filename.endswith(".json"):
# #             with open(os.path.join(DIRECTORY, filename)) as f:
# #                 data = json.load(f)
# #                 tags = data.get('content', {}).get('tags', [])
# #                 for tag in tags:
# #                     if tag not in unique_tags:
# #                         with open("unique_tags.txt", "a") as file:
# #                             file.write(f"{tag}, ")
# #                         unique_tags.append(tag)
# #                     else:
# #                         print(f"skipped duplicate tag: {tag}")
# #     # return unique tags
# #     return unique_tags

# # DIRECTORY="../../../data/cleandata/"
# # unique_tags = get_unique_tags(DIRECTORY)
# # print(f"total unique tags: {len(unique_tags)}")
# # print(f"unique tags = {unique_tags[:10]}")
