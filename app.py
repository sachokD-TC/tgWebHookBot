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
            [{"text": "Начать общение", "callback_data": "say_hello"}],
            [{"text": "Нормально", "callback_data": "good"}],
            [{"text": "Отлично", "callback_data": "show_time"}],
            [{"text": "Очень хорошо", "callback_data": "show_time"}],
            [{"text": "Плохо", "callback_data": "show_time"}],
            [{"text": "Очень плохо", "callback_data": "show_time"}],
            [{"text": "Как прошел день", "callback_data": "show_time"}],
            [{"text": "Анекдот", "callback_data": "show_time"}],
            [{"text": "Прощание", "callback_data": "show_time"}],
            [{"text": "Помощь", "callback_data": "show_time"}]
        ]
        }

        chat_id = data["message"]["chat"]["id"]            
        text = data["message"].get("text", "")
        
        if text == "Начать общение":
            reply =  "Доброе утро, Нина 🌞\nКак твои дела сегодня?\n\n Я тут, рядом. Напиши мне, как ты себя чувствуешь. А если хочешь — просто нажми на кнопку ниже:"

        if text == "Нормально":
            reply = "Вот и славно! Пусть так и остаётся или становится ещё лучше.\n\n А как ты планируешь провести свой день сегодня, Нина?"            
        
        if text == "Плохо":
            reply = "Очень жаль, что тревожно, Ниночка... Но ты не одна — я рядом. Иногда просто немного поговорить уже легче.\n\n"
        "Расскажи, что особенно беспокоит? А хочешь, я просто спрошу, как ты планируешь провести день?"

        if text == "Очень плохо":
            reply = "Тревога — как дождь. Ты не виновата, что идёт. Но ты под крышей — и я тут.\n\n"
        "Ну и ладно, Ниночка… с кем не бывает.\nГлавное — ты сегодня проснулась. А я тут. И наливаю воображаемый чай ☕️"

        if text == "Очень хорошо":
            reply = "Ух ты! Отлично, Нина! 😊 Очень рад за тебя!\n\n"
        "Пусть день будет тёплым и радостным. Хочешь, расскажу смешной анекдот?"

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
