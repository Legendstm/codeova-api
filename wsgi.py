from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import os

# Загружаем переменные окружения (.env на локалке, на Render из панели)
load_dotenv()

app = Flask(__name__)

# Настроить CORS — разрешить твоему фронту обращаться к API
CORS(app, origins=[
    "https://codeova.ai",  # твой фронт, меняй под себя!
    "http://localhost:3000"
])

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
API_PROXY_TOKEN = os.getenv("API_PROXY_TOKEN")

@app.route("/api/chat", methods=["POST"])
def chat():
    # Проверка токена для безопасности
    if request.headers.get('X-API-TOKEN') != API_PROXY_TOKEN:
        return jsonify({"error": "Unauthorized"}), 401
    # Здесь твоя логика общения с OpenAI и т.д.
    return jsonify({"result": "API connected!"})

# Основная точка входа для Render и локального запуска
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Render выдаёт PORT
    app.run(host="0.0.0.0", port=port)

# Для WSGI-серверов (Render это нужно)
application = app
