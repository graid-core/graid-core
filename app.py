from flask import Flask, request, jsonify
from core_grand import process

app = Flask(__name__)

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_input = data.get("user_input", "")

    if not user_input:
        return jsonify({"error": "მომხმარებლის შეტყობინება ცარიელია."}), 400

    response = process(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
