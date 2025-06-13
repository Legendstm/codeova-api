from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import os

# Загрузка переменных окружения
load_dotenv()

app = Flask(__name__)

# Включить CORS для фронта (или для всех на время тестов: origins="*")
CORS(app, origins=["https://codeova.ai", "https://www.codeova.ai"])

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
API_PROXY_TOKEN = os.getenv("API_PROXY_TOKEN")

@app.route("/api/chat", methods=["POST"])
def chat():
    # Проверка токена
    if request.headers.get("X-API-TOKEN") != API_PROXY_TOKEN:
        return jsonify({"error": "Unauthorized"}), 401
    # Твой основной код тут, сейчас тестовый возврат:
    return jsonify({"result": "API connected!"})

# Ключевая строка для WSGI серверов
application = app
