import telebot
from core.config import TOKEN 
from pprint import pprint

bot = telebot.TeleBot(token = TOKEN) 

@bot.message_handler(content_types = ["text"])
def get_message(message):

    if message.text.lower() == "привет":
        bot.send_message(message.chat.id, "Привет, чем могу помочь? ")
        print(message)
    elif message.text.lower() == "/help":
        bot.send_message(message.chat.id, "Здороваться тебя учили? ")
    else: 
        bot.send_message(message.chat.id, "Пока я не знаком с этой фразой")

bot.polling(non_stop = True) 


# list, dictionary, set
# int, float, string, tuple, None


