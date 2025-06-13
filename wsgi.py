from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import os

# Загружаем переменные окружения
load_dotenv()

app = Flask(__name__)
CORS(app, origins=["*"])  # временно для всех, потом можно ограничить

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
API_PROXY_TOKEN = os.getenv("API_PROXY_TOKEN")

@app.route("/api/chat", methods=["POST"])
def chat():
    if request.headers.get('X-API-TOKEN') != API_PROXY_TOKEN:
        return jsonify({"error": "Unauthorized"}), 401
    return jsonify({"result": "API connected!"})

application = app  # В
