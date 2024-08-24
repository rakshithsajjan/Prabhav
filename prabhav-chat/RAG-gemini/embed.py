import os
import json
import logging
from dotenv import load_dotenv
import google.generativeai as genai
from pinecone import Pinecone, ServerlessSpec
import unicodedata
import re
import uuid

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Load environment variables
env_path = os.path.join(os.path.dirname(__file__), '..', 'config', '.env')
load_dotenv(dotenv_path=env_path)

# Configure Gemini API
GOOGLE_API_KEY = os.getenv('GEMINI_API_KEY')
if not GOOGLE_API_KEY:
    raise ValueError("GEMINI_API_KEY not found in environment variables")
genai.configure(api_key=GOOGLE_API_KEY)

# Configure Pinecone
PINECONE_API_KEY = os.getenv('PINECONE_API_KEY')
if not PINECONE_API_KEY:
    raise ValueError("PINECONE_API_KEY not found in environment variables")
pc = Pinecone(api_key=PINECONE_API_KEY)

# Create or connect to a Pinecone index
index_name = "prabhav-chat-index"
try:
    if index_name not in pc.list_indexes():
        pc.create_index(
            name=index_name,
            dimension=768,  # Dimension of Gemini embeddings
            metric="cosine",
            spec=ServerlessSpec(
                cloud="aws",
                region="us-east-1"
            )
        )
    index = pc.Index(index_name)
except Exception as e:
    logging.error(f"Error creating/connecting to Pinecone index: {e}")
    raise

def generate_embedding(text):
    try:
        result = genai.embed_content(
            model="models/text-embedding-004",
            content=text,
            task_type="retrieval_document"
        )
        return result['embedding']
    except Exception as e:
        logging.error(f"Error generating embedding: {e}")
        return None

def clean_title(title):
    # Normalize Unicode characters
    title = unicodedata.normalize('NFKD', title)
    # Replace non-ASCII characters with their closest ASCII equivalents or remove them
    title = re.sub(r'[^\x00-\x7F]+', '', title)
    # Remove any remaining special characters and extra whitespace
    title = re.sub(r'[^\w\s-]', '', title).strip()
    return title

def clean_filename(filename):
    # Remove the file extension
    filename = os.path.splitext(filename)[0]
    # Replace non-alphanumeric characters with underscores
    cleaned = re.sub(r'[^a-zA-Z0-9]', '_', filename)
    # If the cleaned filename is empty, use a UUID
    return cleaned if cleaned else str(uuid.uuid4())

def process_and_store_embeddings(directory):
    file_count = 0
    for filename in os.listdir(directory):
        if filename.endswith(".json"):
            file_path = os.path.join(directory, filename)
            try:
                with open(file_path, 'r') as file:
                    data = json.load(file)
                    content = json.dumps(data.get('content', {}))  # Convert content to string
                    embedding = generate_embedding(content)
                    if embedding:
                        tags = data.get('content', {}).get('tags', [])
                        title = data.get('content', {}).get('title', '')
                        title = clean_title(title)
                        doc_id = data.get('id', '')
                        
                        # Clean the filename to use as vector ID
                        clean_id = clean_filename(filename)
                        
                        vector = {
                            "id": clean_id,
                            "values": embedding,
                            "metadata": {
                                "title": title,
                                "tags": tags,
                                "doc_id": doc_id,
                                "filename": filename
                            }
                        }
                        
                        # Upsert the single vector
                        index.upsert(vectors=[vector])
                        logging.info(f"Upserted vector for file: {filename} with ID: {clean_id}")
                        
                        file_count += 1
                        if file_count % 20 == 0:
                            logging.info(f"Processed {file_count} files")
            except Exception as e:
                logging.error(f"Error processing file {filename}: {e}")
    
    logging.info(f"Total files processed: {file_count}")

if __name__ == "__main__":
    json_directory = "/Users/rakshithsajjan/Desktop/Prabhav/prabhav-chat/RAG-gemini/cleandata"
    process_and_store_embeddings(json_directory)
    logging.info("All files processed and stored in Pinecone.")