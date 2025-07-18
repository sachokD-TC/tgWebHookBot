from flask import Flask, request
import requests
import os

app = Flask(__name__)
TOKEN = os.environ.get("BOT_TOKEN")


@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    print(f"inside webhook")
    data = request.get_json()    
    if "message" in data:
        chat_id = data["message"]["chat"]["id"]            
        text = data["message"].get("text", "")
        if "/start" in text:
            postReply(chat_id, "Доброе утро, Нина 🌞\nКак твои дела сегодня?\n\n"
        "Я тут, рядом. Напиши мне, как ты себя чувствуешь. "
        "А если хочешь — просто нажми на кнопку ниже:")                
    return {"ok": True}

def postReply(chat_id, reply):
    requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", json={
            "chat_id": chat_id,
            "text": reply
        })


@app.route("/")
def index():
    return "Telegram bot is running!"

if __name__ == "__main__":   
    print(f"token - {TOKEN}")
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

