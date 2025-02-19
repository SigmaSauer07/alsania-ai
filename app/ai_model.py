import json
from transformers import AutoModelForCausalLM, AutoTokenizer
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get the Hugging Face access token
access_token = os.getenv('HUGGINGFACE_TOKEN')

# Load GPT-Neo model
model_name = "EleutherAI/gpt-neo-125M"  # Change this to your desired model size
model = AutoModelForCausalLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

print("✅ GPT-Neo model is ready!")

def process_message(user_input):
    inputs = tokenizer(user_input, return_tensors="pt")
    outputs = model.generate(**inputs, max_length=200)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return {"response": response}