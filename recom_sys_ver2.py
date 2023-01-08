import telebot, requests
from telebot import types
bot = telebot.TeleBot('5802011807:AAFJvAo18aWXMf180bhVNvDmNkP-4TDeCPc')

@bot.message_handler(commands=['start'])

def start(message):
    msg=bot.send_message(message.chat.id, f'Здравствуйте, {message.from_user.first_name}', reply_markup=types.ReplyKeyboardRemove())
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("☃ Клиент 1")
    btn2 = types.KeyboardButton("🎄 Клиент 2")
    btn3 = types.KeyboardButton("🎉 Клиент 3")
    btn4 = types.KeyboardButton("🎁 Клиент 4")
    btn5 = types.KeyboardButton("❄ Клиент 5")
    markup.add(btn1, btn2, btn3, btn4, btn5)
    msg=bot.send_message(message.chat.id, 'Выберите клиента для получения рекомендации с помощью кнопки', reply_markup=markup)
    bot.register_next_step_handler(msg,first_request)

@bot.message_handler(content_types=['text'])

def first_request(message):
    if (message.text == "/start"):
        start(message)
    elif(message.text == "☃ Клиент 1"):
        response = requests.post('http://localhost/lgi/Service.svc/Rest/test1/RecomSystem', json={ "DataSet": { "Rows": [{ "ClientID": "94153710"}]}})
        a=response.json()
        b = a["DataSet"]["Rows"]
        for result in b:
            msg1=bot.send_message(message.chat.id,
            f'Клиент: `{result["ClientID"]}`\n\nРекомендации: `{result["Category"]}`', parse_mode='markdown')
            bot.register_next_step_handler(msg1,first_request)
    elif(message.text == "🎄 Клиент 2"):
        response = requests.post('http://localhost/lgi/Service.svc/Rest/test1/RecomSystem', json={ "DataSet": { "Rows": [{ "ClientID": "91600492"}]}})
        a=response.json()
        b = a["DataSet"]["Rows"]
        for result in b:
            msg1=bot.send_message(message.chat.id,
            f'Клиент: `{result["ClientID"]}`\n\nРекомендации: `{result["Category"]}`', parse_mode='markdown')
            bot.register_next_step_handler(msg1,first_request)
    elif(message.text == "🎉 Клиент 3"):
        response = requests.post('http://localhost/lgi/Service.svc/Rest/test1/RecomSystem', json={ "DataSet": { "Rows": [{ "ClientID": "1317148"}]}})
        a=response.json()
        b = a["DataSet"]["Rows"]
        for result in b:
            msg1=bot.send_message(message.chat.id,
            f'Клиент: `{result["ClientID"]}`\n\nРекомендации: `{result["Category"]}`', parse_mode='markdown')
            bot.register_next_step_handler(msg1,first_request)
    elif(message.text == "🎁 Клиент 4"):
        response = requests.post('http://localhost/lgi/Service.svc/Rest/test1/RecomSystem', json={ "DataSet": { "Rows": [{ "ClientID": "539001"}]}})
        a=response.json()
        b = a["DataSet"]["Rows"]
        for result in b:
            msg1=bot.send_message(message.chat.id,
            f'Клиент: `{result["ClientID"]}`\n\nРекомендации: `{result["Category"]}`', parse_mode='markdown')
            bot.register_next_step_handler(msg1,first_request)
    elif(message.text == "❄ Клиент 5"):
        response = requests.post('http://localhost/lgi/Service.svc/Rest/test1/RecomSystem', json={ "DataSet": { "Rows": [{ "ClientID": "584676"}]}})
        a=response.json()
        b = a["DataSet"]["Rows"]
        for result in b:
            msg1=bot.send_message(message.chat.id,
            f'Клиент: `{result["ClientID"]}`\n\nРекомендации: `{result["Category"]}`', parse_mode='markdown')
            bot.register_next_step_handler(msg1,first_request)
    else:
        msg3=bot.send_message(message.chat.id, 'Такого клиента не существует')
        bot.register_next_step_handler(msg3,first_request)

bot.infinity_polling(timeout=10, long_polling_timeout = 5)