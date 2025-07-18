from flask import Flask, request
import requests
import os

app = Flask(__name__)
TOKEN = os.environ.get("BOT_TOKEN")


@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    print(f"inside webhook")
    data = request.get_json()
    print(f"data - {port}")
    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"].get("text", "")
        reply = f"You said: {text}"
        requests.post(f"https://tgwebhookbot.onrender.com/{TOKEN}/sendMessage", json={
            "chat_id": chat_id,
            "text": reply
        })
    return {"ok": True}

@app.route("/")
def index():
    return "Telegram bot is running!"

if __name__ == "__main__":   
    print(f"token - {TOKEN}")
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

