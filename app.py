from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def hello():
    return "Flask app is alive 🧠🔥"

@app.route("/ai-status", methods=["GET"])
def ai_status():
    return jsonify({
        "key": "ai_prediction",
        "value": "running AI to predict next buy"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3432)  # שיניתי את הפורט ל-3432
