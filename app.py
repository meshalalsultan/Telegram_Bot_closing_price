import os

import telebot

BOT_TOKEN = "6128438205:AAEYhtnqD9w5KogC75-vnMA1Mx-zRt1M4KQ"

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")
    
@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, message.text)
    

@bot.message_handler(commands=['youtube','Youtube'])
def send_youtube(message):
    bot.reply_to(message, "Youtube Link =>\
    https://www.youtube.com/")


bot.infinity_polling()
