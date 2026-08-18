import os

from anthropic import Anthropic
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

MODEL = "claude-opus-5"


def get_client():
    return Anthropic()  # reads ANTHROPIC_API_KEY from env


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/health")
def health():
    return jsonify(status="ok"), 200


@app.route("/api/ask", methods=["POST"])
def ask():
    data = request.get_json(silent=True) or {}
    prompt = (data.get("prompt") or "").strip()
    if not prompt:
        return jsonify(error="prompt is required"), 400

    try:
        client = get_client()
        response = client.messages.create(
            model=MODEL,
            max_tokens=1024,
            messages=[{"role": "user", "content": prompt}],
        )
        text = next((b.text for b in response.content if b.type == "text"), "")
        return jsonify(response=text)
    except Exception as e:
        return jsonify(error=str(e)), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
