# bot
#   pip install pytelegrambotapi
# Бот на Aiogram
# https://surik00.gitbooks.io/aiogram-lessons/content/chapter1.html
token = '7754696291:AAECZJA-QR_b1_TtXDdmolcq21DMAGAif4Y'

import telebot
from telebot import types

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,
                     'Я запущен и буду повторять за Вами')

@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id,
                     'Я пока всего лишь ваше эхо и умею не много')


@bot.message_handler(content_types=['text'])
def parrot(message):
    if message.text.lower() =='привет':
        bot.send_message(message.chat.id, 'Ну, здорово!!!')
    else:
        bot.send_message(message.chat.id, message.text)


bot.infinity_polling(none_stop=True)