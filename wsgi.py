from flask import Flask, request, jsonify
import os

app = Flask(__name__)

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "none")
API_PROXY_TOKEN = os.getenv("API_PROXY_TOKEN", "none")

@app.route("/api/chat", methods=["POST"])
def chat():
    if request.headers.get('X-API-TOKEN') != API_PROXY_TOKEN:
        return jsonify({"error": "Unauthorized"}), 401
    return jsonify({"result": "API connected!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
