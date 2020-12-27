import telebot

keyboard = telebot.types.ReplyKeyboardMarkup()
keyboard.row('Привет', 'Пока')

bot = telebot.TeleBot("1492450911:AAGpYNKiCQc0T5WXFQmdB2nhTqarF-zMJB4")

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Хеллоу хуман", reply_markup=keyboard)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, "Привет человек")
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, "Пока человек")

bot.polling()



