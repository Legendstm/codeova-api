from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import os

# Загружаем переменные окружения
load_dotenv()

app = Flask(__name__)

# Включаем CORS только для своего фронта (или "*" если нужно временно открыть для всех)
CORS(app, origins=["https://codeova.ai", "https://www.codeova.ai"])

# Получаем переменные окружения
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
API_PROXY_TOKEN = os.getenv("API_PROXY_TOKEN")

@app.route("/api/chat", methods=["POST"])
def chat():
    # Проверка токена
    if request.headers.get('X-API-TOKEN') != API_PROXY_TOKEN:
        return jsonify({"error": "Unauthorized"}), 401
    # Тут твоя логика общения с OpenAI (заглушка для проверки)
    return jsonify({"result": "API connected!"})

# Ключевая строка для WSGI серверов (Render)
application = app
