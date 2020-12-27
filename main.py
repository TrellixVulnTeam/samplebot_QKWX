# импортируем библиотеку telebot
import telebot
from telebot import types

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
def get_commands_keyboard():
    command_select = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=False)
    command_select.row('start')
    command_select.row('Привет', 'Пока')
    command_select.row('help')

    return command_select


# декоратор для команды /start
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Хеллоу хуман", reply_markup=get_commands_keyboard())


# декоратор для текста
@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, "Привет человек")
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, "Пока человек")


# хелп страница
@bot.message_handler(commands=['help'])
def command_help(m):
    cid = m.chat.id
    help_text = 'Доступны следующие команды \n'
    for key in commands:
        help_text += '/' + key + ': '
        help_text += commands[key] + '\n'
    bot.send_message(cid, help_text, reply_markup=get_commands_keyboard())

    help_text = ('Описание кнопок: \nКнопка "привет" выводит текст "привет человек",'
                 'а кнопка "пока" выводит текст "пока человек"\n')
    bot.send_message(cid, help_text, reply_markup=get_commands_keyboard())
    guide_url = "@fuccbwoi"
    help_text = 'Более подробную инструкцию и помощь вы сможеет узнать  написав мне: {}'.format(guide_url)
    bot.send_message(cid, help_text, reply_markup=get_commands_keyboard())


# для работы нон стоп
bot.polling(none_stop=True)
