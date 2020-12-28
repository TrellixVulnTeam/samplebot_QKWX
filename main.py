# импортируем библиотеку telebot
import telebot
from pyowm import OWM
from telebot import types

# указываем город
city = 'Antarctica'
standart_city = 'Antarctica'
# указываем токен бота
bot = telebot.TeleBot("1492450911:AAGpYNKiCQc0T5WXFQmdB2nhTqarF-zMJB4")
# указываем токен с OWM
owm = OWM('1f538e669ad80922525da0924ecd2375')
# менеджер для работы
manager = owm.weather_manager()
# наблюдение за городом
observation = manager.weather_at_place(city)
# смотрим
view = observation.weather

# описание команд использующееся в команде /help
commands = {
    'start': 'стартовое сообщение и вывод клавиатуры',
    'привет': 'ответ бота на данное сообщение',
    'пока': 'ответ бота на данное сообщение'
}

# создаем клавиатуру
def get_commands_keyboard():
    command_select = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=False)
    command_select.row('/start')
    command_select.row('Привет', 'Пока')
    command_select.row('/help')

    return command_select


# декоратор для команды /start
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Хеллоу хуман", reply_markup=get_commands_keyboard())

# декоратор для команды /help
@bot.message_handler(commands=['help'])
def command_help(m):
    # заменяем message.chat.id на cid
    cid = m.chat.id
    # первая строка для помощи
    help_text = 'Доступны следующие команды \n'
    # перебираем список команд
    for key in commands:
        help_text += '/' + key + ': '
        help_text += commands[key] + '\n'
    # отправляем команды
    bot.send_message(cid, help_text, reply_markup=get_commands_keyboard())
    # добавляем описание кода
    help_text = ('Описание кнопок: \nКнопка "привет" выводит текст "привет человек",'
                 'а кнопка "пока" выводит текст "пока человек"\n')
    bot.send_message(cid, help_text, reply_markup=get_commands_keyboard())
    # указываем ссылку на профиль
    guide_url = "@fuccbwoi"
    help_text = 'Более подробную инструкцию и помощь вы сможеет узнать  написав мне: {}'.format(guide_url)
    bot.send_message(cid, help_text, reply_markup=get_commands_keyboard())


# декоратор для текста
@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, "Привет человек")
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, "Пока человек")

# для работы нон стоп
bot.polling(none_stop=True)
