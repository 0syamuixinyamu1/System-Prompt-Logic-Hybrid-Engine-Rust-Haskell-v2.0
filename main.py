# これを genai.configure(...) の代わりに試してみてください
import google.generativeai as genai

# 直接 Vercel の環境変数から読み込む
api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)

# モデルの初期化（名前を models/ なしで試すのもアリです）
model = genai.GenerativeModel("gemini-1.5-flash")
