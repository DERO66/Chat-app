from fastapi import FastAPI
from pydantic import BaseModel
import os
import requests

app = FastAPI()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_URL = "https://api.openai.com/v1/chat/completions"

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
async def chat(req: ChatRequest):
    if not OPENAI_API_KEY:
        return {"error": "API key is not configured"}
    payload = {
        "model": "gpt-4o-mini",
        "messages": [{"role": "user", "content": req.message}],
        "max_tokens": 800
    }
    headers = {"Authorization": f"Bearer {OPENAI_API_KEY}"}
    r = requests.post(OPENAI_URL, json=payload, headers=headers)
    return r.json()
