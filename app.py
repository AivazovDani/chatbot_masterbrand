from fastapi import FastAPI, Request
import requests
import os

app = FastAPI()

HF_TOKEN = os.getenv("chatbot")  # Set this in Render Dashboard

API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.1"
headers = {"Authorization": f"Bearer {HF_TOKEN}"}

@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    prompt = data.get("prompt", "")
    
    response = requests.post(API_URL, headers=headers, json={
        "inputs": prompt
    })

    if response.status_code != 200:
        return {"error": "Model API failed", "details": response.text}

    result = response.json()
    return {"response": result}
