from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from transformers import pipeline
import os

app = FastAPI()

# Allow frontend domains (like Hugging Face)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this to only your domain in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load your model (you can use Mistral, GPT2, etc.)
pipe = pipeline("text-generation", model="mistralai/Mistral-7B-Instruct-v0.1")

@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    user_input = data.get("message", "")
    
    result = pipe(user_input, max_new_tokens=100, do_sample=True)
    return {"response": result[0]['generated_text']}
