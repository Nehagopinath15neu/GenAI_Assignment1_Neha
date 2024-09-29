import requests
import json

# Function to interact with the LLM API
def call_llm(model_name, user_input, temperature=0.7, max_tokens=100):
    url = "http://localhost:11434/api/chat"  # Ollama API URL
    payload = {
        "model": model_name,
        "temperature": temperature,
        "max_tokens": max_tokens,
        "messages": [
            {"role": "user", "content": user_input.strip()}
        ]
    }

    # Send the request and get the response
    response = requests.post(url, json=payload, stream=True)
    full_response = ""
    
    # Handle streamed response from the model
    for chunk in response.iter_lines():
        if chunk:
            chunk_data = json.loads(chunk.decode("utf-8"))
            full_response += chunk_data.get("message", {}).get("content", "")
            if chunk_data.get("done", False):
                break
    return full_response

# Function to preprocess user input
def preprocess_query(query):
    return query.lower().strip()

# Function to post-process LLM response
def postprocess_response(response):
    return response.strip()

# Function to get a response from the LLM
def get_llm_response(model_name, user_query):
    preprocessed_query = preprocess_query(user_query)
    raw_response = call_llm(model_name, preprocessed_query)
    return postprocess_response(raw_response)

