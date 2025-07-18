from flask import Flask, request
import requests
import os

app = Flask(__name__)
TOKEN = os.environ.get("BOT_TOKEN")


@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    print(f"inside webhook")
    data = request.get_json()            
    
    keyboard = {
        "inline_keyboard": [
            [{"text": "Say Hello", "callback_data": "say_hello"}],
            [{"text": "Show Time", "callback_data": "show_time"}]
        ]
    }
    requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", json={
        "chat_id": chat_id,
        "text": "Choose an action:",
        "reply_markup": keyboard
    })

    if "callback_query" in data:
        chat_id = data["callback_query"]["message"]["chat"]["id"]
        callback_data = data["callback_query"]["data"]

        if callback_data == "say_hello":
        reply = "👋 Hello there!"
        elif callback_data == "show_time":
            from datetime import datetime
            reply = f"🕒 Current time: {datetime.now().strftime('%H:%M:%S')}"
        else:
            reply = "❓ Unknown action."

    requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", json={
        "chat_id": chat_id,
        "text": reply
    })

    if "message" in data:        
        chat_id = data["message"]["chat"]["id"]            
        text = data["message"].get("text", "")
        keyboard = {
            "inline_keyboard": [
                [{"text": "Старт", "url": "https://example.com"}],
                [{"text": "Хорошо", "callback_data": "Как прошел день"}]
            ]
        }
    
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

