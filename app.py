from flask import Flask, request, jsonify
from core_grand import process

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "✅ GRAID LIVE - API მზადაა გამოყენებისთვის"

@app.route("/graid", methods=["POST"])
def handle_input():
    data = request.json
    user_input = data.get("message", "")
    response = process(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
