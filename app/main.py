from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="Alsania AI Chatbot")

app.include_router(router)

@app.get("/")
def home():
    return {"message": "Welcome to the Alsania AI Chatbot!"}
