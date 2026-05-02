import requests
import os

API_KEY = os.getenv("DEEPSEEK_API_KEY")
URL = "https://api.deepseek.com/chat/completions"

def ask_deepseek(prompt):
    response = requests.post(URL, 
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "deepseek-chat",
            "messages": [{"role": "user", "content": prompt}]
        }
    )
    data = response.json()
    return data["choices"][0]["message"]["content"]

print(ask_deepseek("What is an AI agent in one paragraph?"))