import telebot
from lib import *

token = (open("./token", "r")).read()   
bot = telebot.TeleBot(token)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши название лекарства")
    if '!' in message.text[-1]:
        drug_name = message.text.replace('!', '')
        try:
            bot.send_photo(message.from_user.id, return_chemical_form_of(drug_name))
        except IndexError:
            bot.send_message(message.from_user.id, "Такое лекарство не найдено! Попробуйте снова.")
    else:
        bot.send_message(message.from_user.id, "Напиши /help.")

bot.polling(none_stop=True, interval=0)