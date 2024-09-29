# import requests
# import json

# url = "http://localhost:11434/api/chat"

# # Payload for simple query
# payload = {
#     "model": "mistral",
#     "temperature": 0.5,
#     "max_tokens": 50,
#     "messages": [
#         { "role": "user", "content": "What is the capital of Japan?" }
#     ]
# }

# # Streaming response to handle chunked responses
# response = requests.post(url, json=payload, stream=True)

# full_response = ""
# for chunk in response.iter_lines():
#     if chunk:
#         chunk_data = json.loads(chunk.decode("utf-8"))
#         full_response += chunk_data.get("message", {}).get("content", "")
#         if chunk_data.get("done", False):
#             break

# print("Mistral Model response (Simple Query):", full_response)

# import requests
# import json

# url = "http://localhost:11434/api/chat"

# # Payload for a multi-turn conversation
# payload = {
#     "model": "mistral",
#     "temperature": 0.6,
#     "max_tokens": 100,
#     "messages": [
#         { "role": "user", "content": "Can you explain what quantum mechanics is?" },
#         { "role": "user", "content": "How is it different from classical physics?" },
#         { "role": "user", "content": "Can you give an example of quantum mechanics in everyday life?" }
#     ]
# }

# # Streaming response to handle chunked responses
# response = requests.post(url, json=payload, stream=True)

# full_response = ""
# for chunk in response.iter_lines():
#     if chunk:
#         chunk_data = json.loads(chunk.decode("utf-8"))
#         full_response += chunk_data.get("message", {}).get("content", "")
#         if chunk_data.get("done", False):
#             break

# print("Mistral Model response (Multi-Turn Conversation):", full_response)

# import requests
# import json

# url = "http://localhost:11434/api/chat"

# # Payload with different parameters
# payload = {
#     "model": "mistral",
#     "temperature": 0.9,  # Higher temperature for more creativity
#     "max_tokens": 150,   # More tokens for a longer response
#     "messages": [
#         { "role": "user", "content": "Write a short story about a dragon that discovers it can fly." }
#     ]
# }

# # Streaming response to handle chunked responses
# response = requests.post(url, json=payload, stream=True)

# full_response = ""
# for chunk in response.iter_lines():
#     if chunk:
#         chunk_data = json.loads(chunk.decode("utf-8"))
#         full_response += chunk_data.get("message", {}).get("content", "")
#         if chunk_data.get("done", False):
#             break

# print("Mistral Model response (Different Parameters):", full_response)


import requests
import json

url = "http://localhost:11434/api/chat"

# Payload for summarization task
payload = {
    "model": "mistral",
    "temperature": 0.5,   # Lower temperature for a more focused answer
    "max_tokens": 60,
    "messages": [
        { "role": "user", "content": "Summarize the following text: 'Artificial intelligence is transforming industries like healthcare, finance, and education by improving decision-making, enhancing efficiency, and enabling automation of tasks that were once too complex for computers.'" }
    ]
}

# Streaming response to handle chunked responses
response = requests.post(url, json=payload, stream=True)

full_response = ""
for chunk in response.iter_lines():
    if chunk:
        chunk_data = json.loads(chunk.decode("utf-8"))
        full_response += chunk_data.get("message", {}).get("content", "")
        if chunk_data.get("done", False):
            break

print("Mistral Model response (Summarization Task):", full_response)

import requests
import json

url = "http://localhost:11434/api/chat"

# Payload for solving a math problem
payload = {
    "model": "mistral",
    "temperature": 0.3,
    "max_tokens": 30,
    "messages": [
        { "role": "user", "content": "What is the square root of 144?" }
    ]
}

# Streaming response to handle chunked responses
response = requests.post(url, json=payload, stream=True)

full_response = ""
for chunk in response.iter_lines():
    if chunk:
        chunk_data = json.loads(chunk.decode("utf-8"))
        full_response += chunk_data.get("message", {}).get("content", "")
        if chunk_data.get("done", False):
            break

print("Mistral Model response (Math Problem Task):", full_response)







