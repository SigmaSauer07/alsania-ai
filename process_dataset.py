from sentence_transformers import SentenceTransformer
import chromadb
import json

# Load embedding model
embedder = SentenceTransformer("all-MiniLM-L6-v2")

# Connect to ChromaDB
chroma_client = chromadb.PersistentClient(path="./chroma_db")
collection = chroma_client.get_or_create_collection("training_data")

# Load dataset from IPFS/IPNS
with open("dataset/dataset.json", "r") as file:
    training_data = json.load(file)

# Process training data and store embeddings
for entry in training_data["training_data"]["messages"]:
    vector = embedder.encode(entry["input"]).tolist()
    collection.add(ids=[entry["input"]], embeddings=[vector], metadatas=[{"response": entry["response"]}])

print("✅ Dataset stored as vectors in ChromaDB!")