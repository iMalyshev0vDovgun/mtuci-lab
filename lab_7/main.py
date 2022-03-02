import telebot
from telebot import types

token = "5022191364:AAF50BNLuTol2SGK2-jU0ppKMgYJ4QLn6XQ"

info = 'Московский технический университет связи и информатики (сокр. МТУСИ) — российский отраслевой университет ' \
       'в области информационных технологий, телекоммуникаций, информационной безопасности.\n\n' \
       'Хочешь узнать больше? Тогда тебе сюда - https://mtuci.ru/'

help = 'Это простой бот с базовой информацией об МТУСИ.\n\n' \
       '    /help   Краткая справка о возможностях.\n' \
       '    /enter  Информация о поступлении.\n' \
       '    /about  Информация для связи.\n'

enter = 'Хочешь поступить, отлично!\nТогда тебе сюда - https://abitur.mtuci.ru/'

about = 'Почта: pk@mtuci.ru\n' \
        'Телефон: +7 (495) 673-36-25 или +7 (495) 957-79-87'

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("Да, хочу!", "/help")
    bot.send_message(message.chat.id, 'Привет! Хочешь узнать свежую информацию о МТУСИ?', reply_markup=keyboard)


@bot.message_handler(commands=['help'])
def start_message(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("/enter", "/about", "/help")
    bot.send_message(message.chat.id, help, reply_markup=keyboard)


@bot.message_handler(commands=['enter'])
def start_message(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("/help")
    bot.send_message(message.chat.id, enter, reply_markup=keyboard)


@bot.message_handler(commands=['about'])
def start_message(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("/help")
    bot.send_message(message.chat.id, about, reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text.lower() == "да, хочу!":
        bot.send_message(message.chat.id, info)
    elif message.text.lower() == "привет":
        bot.send_message(message.chat.id, 'Здравствуй!')
    else:
        bot.send_message(message.chat.id, 'Подобной команды нет, обратитесь к справке - /help')


bot.polling(none_stop=True)