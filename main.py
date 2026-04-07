from fastapi import FastAPI
from pydantic import BaseModel
import google.generativeai as genai  # Googleのライブラリに変更
import os

app = FastAPI()

# ここにあなたの最強プロンプトを全部貼ってください
SYSTEM_PROMPT = """
システムプロンプト：Logic Hybrid Engine (Rust/Haskell) v2.0
...（中略：GitHubにあるあの長いプロンプト）...
"""

# Google APIの初期化
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# モデルの設定（システムプロンプトをここで「脳」に刻み込みます）
model = genai.GenerativeModel(
    model_name="gemini-1.5-pro", # または "gemini-1.5-flash"
    system_instruction=SYSTEM_PROMPT
)

class Query(BaseModel):
    text: str

@app.get("/")
def read_root():
    return {"status": "Logic Hybrid Engine v2.0 (Gemini Edition) is Online"}

@app.post("/ask")
async def ask(query: Query):
    try:
        # Geminiに質問を投げる
        response = model.generate_content(query.text)
        return {"response": response.text}
    except Exception as e:
        return {"error": str(e)}
