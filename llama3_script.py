# import requests
# import json

# url = "http://localhost:11434/api/chat"
# payload = {
#     "model": "llama3",
#     "messages": [
#         { "role": "user", "content": "Why is the sky blue?" }
#     ]
# }

# # Use a streaming response to handle chunked responses
# response = requests.post(url, json=payload, stream=True)

# # Collecting chunks as they arrive
# full_response = ""
# for chunk in response.iter_lines():
#     if chunk:
#         chunk_data = json.loads(chunk.decode("utf-8"))
#         full_response += chunk_data.get("message", {}).get("content", "")
#         if chunk_data.get("done", False):
#             break

# print("Model response:", full_response)

# import requests
# import json

# url = "http://localhost:11434/api/chat"
# payload = {
#     "model": "llama3",
#     "messages": [
#         { "role": "user", "content": "Explain how gravity works." },
#         { "role": "assistant", "content": "Gravity is a force that pulls objects towards one another." },
#         { "role": "user", "content": "How does it affect planetary motion?" },
#         { "role": "assistant", "content": "Gravity keeps planets in orbit around stars." }
#     ]
# }

# # Use a streaming response to handle chunked responses
# response = requests.post(url, json=payload, stream=True)

# # Collecting chunks as they arrive
# full_response = ""
# for chunk in response.iter_lines():
#     if chunk:
#         chunk_data = json.loads(chunk.decode("utf-8"))
#         full_response += chunk_data.get("message", {}).get("content", "")
#         if chunk_data.get("done", False):
#             break

# print("Model response:", full_response)

# import requests
# import json

# url = "http://localhost:11434/api/chat"
# payload = {
#     "model": "llama3",
#     "temperature": 0.7,
#     "max_tokens": 100,
#     "messages": [
#         { "role": "user", "content": "Tell me a short story about a brave knight." }
#     ]
# }

# # Use a streaming response to handle chunked responses
# response = requests.post(url, json=payload, stream=True)

# # Collecting chunks as they arrive
# full_response = ""
# for chunk in response.iter_lines():
#     if chunk:
#         chunk_data = json.loads(chunk.decode("utf-8"))
#         full_response += chunk_data.get("message", {}).get("content", "")
#         if chunk_data.get("done", False):
#             break

# print("Model response:", full_response)


import requests
import json

url = "http://localhost:11434/api/chat"
payload = {
    "model": "llama3",
    "temperature": 0.5,
    "max_tokens": 50,
    "messages": [
        { "role": "user", "content": "Summarize the following text: 'Artificial intelligence is rapidly growing and changing the landscape of various industries. It is used in fields such as healthcare, finance, and education to improve decision-making and efficiency.'" }
    ]
}

# Use a streaming response to handle chunked responses
response = requests.post(url, json=payload, stream=True)

# Collecting chunks as they arrive
full_response = ""
for chunk in response.iter_lines():
    if chunk:
        chunk_data = json.loads(chunk.decode("utf-8"))
        full_response += chunk_data.get("message", {}).get("content", "")
        if chunk_data.get("done", False):
            break

print("Model response:", full_response)


