from flask import Flask, request
import requests
import os

app = Flask(__name__)
TOKEN = os.environ.get("BOT_TOKEN")    


def main_keyboard():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(KeyboardButton("Привіт 👋"), KeyboardButton("Допомога ❓"))
    return markup



@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    data = request.get_json()       
    reply = None
    if "message" in data:        
        
        keyboard = {
        "keyboard": [
            [{"text": "Say Hello", "callback_data": "say_hello"}],
            [{"text": "Хорошо", "callback_data": "good"}],
            [{"text": "Show Time", "callback_data": "show_time"}]

        ]
        }

        chat_id = data["message"]["chat"]["id"]            
        text = data["message"].get("text", "")
        
        if text == "Say Hello":
            reply =  "Доброе утро, Нина 🌞\nКак твои дела сегодня?\n\ Я тут, рядом. Напиши мне, как ты себя чувствуешь. А если хочешь — просто нажми на кнопку ниже:"
                                 
        if reply != None:   
            requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", json={
                "chat_id": chat_id,
                "text": reply
            })
    
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
