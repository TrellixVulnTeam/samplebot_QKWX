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
    command_select.row('/get_city', '/weather')
    command_select.row('/temp', '/humidity')
    command_select.row('/pressure')

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

# декоратор для получения текущего города
@bot.message_handler(commands=["get_city"])
def get_city(message):
    bot.send_message(message.chat.id, f"Текущий город: {city}")

# декоратор для получения температуры
@bot.message_handler(commands=['temp'])
def get_temperature(message):
    bot.send_message(message.chat.id, f"""Температура: {view.temperature('celsius').get('temp')}°C
Ощущается как: {view.temperature('celsius').get('feels_like')}°C""")

# декоратор для получения влажности
@bot.message_handler(commands=['humidity'])
def get_humidity(message):
    bot.send_message(message.chat.id, f"Влажность: {view.humidity}%")

# декоратор для получения атмосферного давления
@bot.message_handler(commands=['pressure'])
def get_pressure(message):
    bot.send_message(message.chat.id, "Атмосферное давление: {} мм рт. ст.".format(int(view.pressure.get("press"))))

# декоратор для получения полного списка характеристик погоды
@bot.message_handler(commands=['weather'])
def get_weather(message):
    bot.send_message(message.chat.id,
                     f"""Полные сведения о погоде:
Город: {city}
Температура: {view.temperature('celsius').get("temp")}°C
Минимальная температура: {view.temperature('celsius').get("temp_min")}°C
Максимальная температура: {view.temperature('celsius').get("temp_max")}°C
Атмосферное давление: {int(view.pressure.get("press"))} мм рт. ст.
Влажность: {view.humidity}%
Облачность: {view.clouds}%
Ветер м/с: {view.wind}
""")


# для работы нон стоп
bot.polling(none_stop=True)
