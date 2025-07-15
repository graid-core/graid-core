from flask import Flask, request
from core_grand import process

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "✅ GRAID LIVE - API არის მზად გამოყენებისთვის"

@app.route("/graid", methods=["POST"])
def handle_input():
    data = request.json
    user_input = data.get("message", "")
    response = process(user_input)
    return {"response": response}
