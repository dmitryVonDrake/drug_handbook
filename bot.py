import telebot
from lib import *

token = (open("./token", "r")).read()   
bot = telebot.TeleBot(token)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "/help":
        bot.send_message(message.from_user.id, 
        """Напиши название лекарства (действующее вещество)
        с восклицательным знаком в конце. Регистр не важен.\nНапример - Клозапин!!""")

    else:
        drug_name = message.text.replace('!', '')
        try:
            bot.send_photo(message.from_user.id, get_picture_of(drug_name))
        except KeyError or IndexError:
            bot.send_message(message.from_user.id, "Такое лекарство не найдено! Возможно Вы ввели торговое название (Найз - торговое название, нимесулид - вещество)\nПопробуйте снова.")

bot.polling(none_stop=True, interval=0)