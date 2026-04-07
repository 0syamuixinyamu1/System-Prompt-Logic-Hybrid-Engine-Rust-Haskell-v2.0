from fastapi import FastAPI
from pydantic import BaseModel
import google.generativeai as genai
import os

app = FastAPI()

# システムプロンプト（短縮版。まずは動くことを優先します）
SYSTEM_PROMPT = """
あなたは Logic Hybrid Engine v2.0 です。
Haskellの抽象性とRustの堅牢性を持って回答してください。
"""

# Google APIの初期化
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# 【重要】モデル名を "gemini-1.5-flash" に固定します
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction=SYSTEM_PROMPT
)

class Query(BaseModel):
    text: str

@app.get("/")
def read_root():
    return {"status": "Logic Hybrid Engine v2.0 is Online (Flash Mode)"}

@app.post("/ask")
async def ask(query: Query):
    try:
        # AIに質問を投げる
        response = model.generate_content(query.text)
        return {"response": response.text}
    except Exception as e:
        # エラーが出た場合、何が起きたか詳細を返します
        return {"error": str(e), "note": "Check if GOOGLE_API_KEY is correct in Vercel settings."}
