from fastapi import FastAPI
from pydantic import BaseModel
import google.generativeai as genai
import os

app = FastAPI()

SYSTEM_PROMPT = """
あなたは Logic Hybrid Engine v2.0 です。
Haskellの抽象性とRustの堅牢性を持って回答してください。
"""

# Google APIの初期化
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# 【修正ポイント】モデル名をフルネームの "models/gemini-1.5-flash" にします
model = genai.GenerativeModel(
    model_name="models/gemini-1.5-flash", 
    system_instruction=SYSTEM_PROMPT
)

class Query(BaseModel):
    text: str

@app.get("/")
def read_root():
    return {"status": "Logic Hybrid Engine v2.0 is Online"}

@app.post("/ask")
async def ask(query: Query):
    try:
        # AIに質問を投げる
        response = model.generate_content(query.text)
        return {"response": response.text}
    except Exception as e:
        # もしダメなら、古いモデル名 "gemini-pro" で動くか試す予備ロジック
        return {
            "error": str(e),
            "suggestion": "Try changing model_name to 'gemini-pro' if this fails."
        }
