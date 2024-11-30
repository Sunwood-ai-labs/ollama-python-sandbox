"""
Mock Ollama API server for testing and development purposes.
This server simulates the basic functionality of Ollama's API endpoints.
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional, Dict, Any
import uvicorn

app = FastAPI(title="Mock Ollama API")

class ChatMessage(BaseModel):
    role: str
    content: str
    images: Optional[List[str]] = None

class ChatRequest(BaseModel):
    model: str
    messages: List[ChatMessage]
    stream: Optional[bool] = False

class GenerateRequest(BaseModel):
    model: str
    prompt: str
    stream: Optional[bool] = False

class ModelResponse(BaseModel):
    model: str
    created_at: str
    response: str

@app.get("/api/ping")
async def ping():
    return {"status": "ok"}

@app.post("/api/chat")
async def chat(request: ChatRequest):
    # Mock response based on the last message
    last_message = request.messages[-1]
    if "sky blue" in last_message.content.lower():
        response = "The sky appears blue due to a phenomenon called Rayleigh scattering. Sunlight reaches Earth's atmosphere and is scattered in all directions by gases and other particles in the air. Blue light is scattered more than other colors because it travels as shorter waves."
    else:
        response = "I am a mock Ollama API response. This is a sandbox environment for testing the client library."
    
    return {
        "model": request.model,
        "created_at": "2024-11-30T12:00:00.000000Z",
        "message": {
            "role": "assistant",
            "content": response
        }
    }

@app.post("/api/generate")
async def generate(request: GenerateRequest):
    response = f"Mock response for prompt: {request.prompt}"
    return {
        "model": request.model,
        "created_at": "2024-11-30T12:00:00.000000Z",
        "response": response,
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=11434)
