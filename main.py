from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI  # OpenAIのライブラリをインポート
import os

app = FastAPI()

# ここにあなたの「Logic Hybrid Engine v2.0」のプロンプトを全部貼ります
SYSTEM_PROMPT = """
システムプロンプト：Logic Hybrid Engine (Rust/Haskell) v2.0
...（中略：ここにGitHubにあるあの長いプロンプトを全部貼ってください）...
"""

# OpenAIクライアントの初期化（Vercelの環境変数からキーを読み込む）
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class Query(BaseModel):
    text: str

@app.get("/")
def read_root():
    return {"status": "Logic Hybrid Engine v2.0 is Online"}

@app.post("/ask")
async def ask(query: Query):
    try:
        # 本物のAI（GPT-4oなど）を呼び出す
        response = client.chat.completions.create(
            model="gpt-4o",  # または "gpt-3.5-turbo"
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": query.text}
            ]
        )
        # AIの回答だけを抽出して返す
        answer = response.choices[0].message.content
        return {"response": answer}
    
    except Exception as e:
        return {"error": str(e)}
