import json
from transformers import AutoModelForCausalLM, AutoTokenizer
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get the Hugging Face access token
access_token = os.getenv('HUGGINGFACE_TOKEN')

# Load Mistral 7B model with authentication
model_name = "EleutherAI/gpt-neo-125m"
model = AutoModelForCausalLM.from_pretrained(model_name, use_auth_token=access_token, device_map="cpu")
tokenizer = AutoTokenizer.from_pretrained(model_name, use_auth_token=access_token)

print("✅ gpt-neo-125m is ready!")

# Process user input and generate AI response
def process_message(user_input):
    inputs = tokenizer(user_input, return_tensors="pt").to("cuda")  # Move to GPU if available
    outputs = model.generate(**inputs, max_length=200)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return {"response": response}
