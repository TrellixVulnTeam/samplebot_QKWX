# импортируем библиотеку telebot
import telebot
from telebot import  types
# создаем клавиатуру
# keyboard = telebot.types.ReplyKeyboardMarkup(True)
# добавляем кнопки на клавиатуру
# keyboard.row('Привет', 'Пока')
# указываем токен бота
bot = telebot.TeleBot("1492450911:AAGpYNKiCQc0T5WXFQmdB2nhTqarF-zMJB4")
# описание команд использующееся в команде /help
commands = {
    'start': 'стартовое сообщение и вывод клавиатуры',
    'привет': 'ответ бота на данное сообщение',
    'пока': 'ответ бота на данное сообщение'
}
# создаем клавиатуру
def get_commands():
    command_select = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=False)
    command_select.row('/start')
    command_select.row('Привет', 'Пока')
    command_select.row('/help')
    return command_select
# декоратор для команды /start
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Хеллоу хуман", reply_markup=get_commands())
# декоратор для текста
@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, "Привет человек")
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, "Пока человек")
# для работы нон стоп
bot.polling(none_stop=True)



