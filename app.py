from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["GET"])
def home():
    return "✅ GRAID API is live!"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    message = data.get("message", "")
    
    # დროებითი საპასუხო ლოგიკა (შეიცვლება რეალური GRAID core logic-ით)
    reply = f"GRAID received: {message}"
    
    return jsonify({"response": reply})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
