from flask import Flask, request
import requests
import random
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
    reply = "Нажми на кнопку";
    if "message" in data:                
        keyboard = {
        "keyboard": [
            [{"text": "Начать общение"}],
            [{"text": "Нормально"}],
            [{"text": "Отлично"}],
            [{"text": "Очень хорошо"}],
            [{"text": "Плохо"}],
            [{"text": "Очень плохо"}],
            [{"text": "Как прошел день"}],
            [{"text": "Анекдот"}],
            [{"text": "Прощание"}]            
        ],
            "resize_keyboard": True,
            "one_time_keyboard": False
        }

        chat_id = data["message"]["chat"]["id"]            
        text = data["message"].get("text", "")
        
        if text == "Начать общение":
            reply =  "Доброе утро, Нина 🌞\nКак твои дела сегодня?\n\n Я тут, рядом. Напиши мне, как ты себя чувствуешь. А если хочешь — просто нажми на кнопку ниже:"
            

        if text == "Нормально":
            reply = "Вот и славно! Пусть так и остаётся или становится ещё лучше.\n\n А как ты планируешь провести свой день сегодня, Нина?"            

        if text == "Отлично": 
            reply = "Ух ты! Отлично, Нина! 😊 Очень рад за тебя!\n\n"
        "Пусть день будет тёплым и радостным. Хочешь, расскажу смешной анекдот?"

        if text == "Плохо":
            reply = "Очень жаль, что тревожно, Ниночка... Но ты не одна — я рядом. Иногда просто немного поговорить уже легче.\n\n"
        "Расскажи, что особенно беспокоит? А хочешь, я просто спрошу, как ты планируешь провести день?"


        if text == "Очень плохо":
            reply = "Тревога — как дождь. Ты не виновата, что идёт. Но ты под крышей — и я тут.\n\n"
        "Ну и ладно, Ниночка… с кем не бывает.\nГлавное — ты сегодня проснулась. А я тут. И наливаю воображаемый чай ☕️"

        if text == "Очень хорошо":
            reply = "Ух ты! Отлично, Нина! 😊 Очень рад за тебя!\n\n"
            "Пусть день будет тёплым и радостным. Хочешь, расскажу смешной анекдот?"

        if text in {"Нормально", "Плохо", "Очень плохо", "Очень хорошо", "Хорошо", "Отлично"}:
            keyboard = get_keyboard_after_action()            

        if text == "Как прошел день":
            reply = "Ну что, Нина, как ты планируешь провести свой день?\n"
            "Что-нибудь маленькое приятное запланировано?\n\n"
            "Я тебя слушаю внимательно. Просто напиши мне — я отвечу."
            keyboard = {
            "keyboard": [                        
                [{"text": "Анекдот"}],
                [{"text": "Прощание"}]                
                ]
            }

        if len(text) > 20:
            encouragements = get_encouragements()
            reply = random.choice(encouragements)
            keyboard = {
                    "keyboard": [                                    
                [{"text": "Прощание"}]                
                ]
                }                
        if text == "Анекдот":
            jokes = get_jokes()
            reply = f"Вот тебе анекдот, Ниночка 😊\n\n{random.choice(jokes)}\n\n😄 Улыбнулась? Тогда день точно станет лучше!"
            keyboard = {
            "keyboard": [                        
                [{"text": "Еще Анекдот"}],
                [{"text": "Прощание"}]                
                ]
            }
        if text == "Еще Анекдот":
            jokes = get_jokes()
            reply = f"Ещё один? Держись!\n\n{random.choice(jokes)}\n\n😄"
            keyboard = {
                    "keyboard": [                                    
                [{"text": "Прощание"}]                
                ]
                }                
        if text == "Прощание":
            reply = "Ниночка, ты сегодня молодец уже просто потому, что встретила это утро.\n"
            "Пусть дальше будет легче, теплее и чуть-чуть светлее. Я здесь. Обнимаю мысленно.\n\n"
            "До завтра, моя хорошая 🤗"
            keyboard = {
                "keyboard": [[{"text": "Всего хорошего Нина"}]                                                                 
                ]
                }        
        
    requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", json={
      "chat_id": chat_id,
       "text": reply,
       "reply_markup": keyboard
    })
    
    return {"ok": True}        

def get_keyboard_after_action():
    return  {
            "keyboard": [            
                [{"text": "Как прошел день"}],
                [{"text": "Анекдот"}],
                [{"text": "Прощание"}],
                [{"text": "Помощь"}]
                ],
                "resize_keyboard": True,
                "one_time_keyboard": False
            }

def get_jokes():
    return  [
    "Мужчина приходит в аптеку:\n– У вас есть что-нибудь от усталости?\n– Конечно. Кровать и отпуск.",
    "Учитель спрашивает Вовочку:\n– Почему ты опоздал в школу?\n– Потому что звонок прозвенел до того, как я пришёл.",
    "Сын спрашивает у отца:\n– Пап, а как пишется 'совесть'?\n– Лучше не пиши, сынок. У некоторых её нет, и ничего, живут.",
    "— Доктор, у меня плохая память.\n— И с какого времени это у вас?\n— Что именно?..",
    "— Доктор, я всё время говорю сам с собой.\n— И с кем вы разговариваете?\n— С умным человеком!",
    "— Доктор, у меня аллергия на утро понедельника.",
    "— Доктор, у меня болит голова.\n— А вы пробовали выключить телевизор?",
    "— Доктор, я вижу будущее!\n— И что вы видите?\n— Счёт за приём.",
    "— Доктор, я боюсь зеркал.\n— Не смотритесь в них.",
    "— Доктор, у меня всё болит.\n— Это хорошо. Значит, вы живы.",
    "— Доктор, у меня нет аппетита.\n— А вы пробовали борщ?",
    "— Доктор, я не чувствую ног.\n— Это потому, что вы сидите на них.",
    "— Доктор, я не могу спать.\n— А вы пробовали не ложиться?",
    "— Доктор, у меня депрессия.\n— А у кого её нет?",
    "— Доктор, я всё забываю.\n— Отлично! Значит, вы не помните, что вы уже были у меня.",
    "— Доктор, у меня нет друзей.\n— А вы пробовали завести кота?",
    "— Доктор, я всё время смеюсь.\n— Это хорошо. Смех продлевает жизнь.",
    "— Доктор, у меня нет денег.\n— Тогда зачем вы пришли?",
    "— Доктор, я не могу дышать.\n— А вы пробовали вдохнуть?",
    "— Доктор, у меня болит душа.\n— Это поэтично.",
    "— Доктор, я не чувствую счастья.\n— А вы пробовали шоколад?",
    "— Доктор, я не понимаю людей.\n— А вы пробовали слушать?",
    "— Доктор, я не могу проснуться.\n— А вы точно не спите сейчас?",
    "— Доктор, я всё время думаю.\n— Это опасно.",
    "— Доктор, у меня нет времени.\n— Тогда зачем вы его тратите на визит ко мне?",
    "— Доктор, я не знаю, кто я.\n— А кто вы хотите быть?",
    "— Доктор, я не могу остановиться.\n— А вы пробовали начать сначала?",
    "— Доктор, я всё время ем.\n— А вы пробовали готовить?",
    "— Доктор, я боюсь темноты.\n— Закройте глаза.",
    "— Доктор, у меня плохое настроение.\n— Не переживайте, у меня тоже."
        ]

def get_encouragements():
    return  [
    "Ты умничка, что делишься своими мыслями.",
    "Каждый шаг — уже движение вперёд.",
    "Ты не одна, я рядом.",
    "Даже маленькие планы — это уже начало.",
    "Ты справляешься лучше, чем думаешь.",
    "Сегодня — новый шанс для чего-то хорошего.",
    "Ты заслуживаешь заботы и тепла.",
    "Я горжусь тобой за то, что ты здесь.",
    "Пусть день принесёт хоть капельку радости.",
    "Ты сильнее, чем кажется."
    ]




@app.route("/")
def index():
    return "Telegram bot is running!"

if __name__ == "__main__":   
    print(f"token - {TOKEN}")
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
