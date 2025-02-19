import json
from transformers import AutoModelForCausalLM, AutoTokenizer

# Load Mistral 7B model
model_name = "mistralai/Mistral-7B-Instruct-v0.1"
model = AutoModelForCausalLM.from_pretrained(model_name, device_map="auto")
tokenizer = AutoTokenizer.from_pretrained(model_name)

print("✅ Mistral 7B is ready!")

# Process user input and generate AI response
def process_message(user_input):
    inputs = tokenizer(user_input, return_tensors="pt").to("cuda")  # Move to GPU if available
    outputs = model.generate(**inputs, max_length=200)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return {"response": response}
