from sentence_transformers import SentenceTransformer
import chromadb

# Load embedding model
embedder = SentenceTransformer("all-MiniLM-L6-v2")

# Connect to ChromaDB
chroma_client = chromadb.PersistentClient(path="./chroma_db")
collection = chroma_client.get_or_create_collection("training_data")

def get_ai_response(user_input):
    query_vector = embedder.encode(user_input).tolist()
    results = collection.query(query_embeddings=[query_vector], n_results=1)

    if results["ids"]:
        return results["metadatas"][0][0]["response"]
    else:
        return "I'm not sure yet, but I'll learn!"

# Example usage
if __name__ == "__main__":
    user_input = input("You: ")
    ai_response = get_ai_response(user_input)
    print("Alsania AI:", ai_response)
