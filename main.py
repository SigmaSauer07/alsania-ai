import os
from fastapi import FastAPI
from dotenv import load_dotenv
from app.routes import router

# Load environment variables from .env file
load_dotenv()

# Get Hugging Face token from .env (if needed for API requests)
HUGGINGFACE_TOKEN = os.getenv("HUGGINGFACE_TOKEN")

# Initialize FastAPI app
app = FastAPI(title="Alsania AI Chatbot")

# Include your router
app.include_router(router)

# Root endpoint
@app.get("/")
def home():
    return {"message": "Welcome to the Alsania AI Chatbot!"}

# Test environment variable loading
@app.get("/env-check")
def env_check():
    return {"HUGGINGFACE_TOKEN": HUGGINGFACE_TOKEN if HUGGINGFACE_TOKEN else "Token not found"}
