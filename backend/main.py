from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import subprocess
import json

app = FastAPI()

# Allow frontend (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # for dev, restrict for prod
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    prompt: str

@app.post("/chat")
async def chat_endpoint(chat_req: ChatRequest):
    response = subprocess.run(
        ["ollama", "run", "llama3", chat_req.prompt],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    return {"response": response.stdout.strip()}
