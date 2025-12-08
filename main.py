import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
url = "https://openrouter.ai/api/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

user_prompt = input("Enter your prompt: ")

data = {
    "model": "openai/gpt-oss-120b:free",
    "messages": [
        {
            "role": "user",
            "content": user_prompt
        }
    ]
}

response = requests.post(url, headers=headers, json=data)

if response.status_code == 200:
    result = response.json()
    print("\nAnswer:")
    print(result['choices'][0]['message']['content'])
else:
    print(f"Error: {response.status_code}")
    print(response.text)