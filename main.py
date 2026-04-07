from fastapi import FastAPI
from pydantic import BaseModel
import os

app = FastAPI()

SYSTEM_PROMPT = "ここにGitHubにあるプロンプト全文を貼る"

@app.get("/")
def read_root():
    return {"status": "Logic Hybrid Engine v2.0 is Online"}

@app.post("/ask")
async def ask(data: dict):
    # ここにLLM（OpenAI等）を呼び出すコードを数行書くだけです
    return {"message": "Engine is processing...", "input": data}
