from telebot import *
import emoji

bot = telebot.TeleBot('6593889559:AAFEnaxI9L85QmLfyXmYOycnEzpXFpaeRTk', parse_mode=None)


@bot.message_handler(commands=['start', 'main', 'hello'])
def main(message):
    bot.send_message(message.from_user.id, f"Привіт {message.from_user.first_name}!")
    markup = types.ReplyKeyboardMarkup()
    buckwheat = types.KeyboardButton(emoji.emojize('🫕 Гречана'))
    rice = types.KeyboardButton(emoji.emojize('🍚 Рис'))
    oatmeal = types.KeyboardButton(emoji.emojize('🥣 Вівсяна'))
    pasta = types.KeyboardButton(emoji.emojize('🍝 Макарони'))
    corn = types.KeyboardButton(emoji.emojize('🌽 Кукурудзяна'))
    pearl_barley = types.KeyboardButton(emoji.emojize('🍲 Перлова'))
    markup.row(buckwheat, rice, oatmeal)
    markup.row(pasta, corn, pearl_barley)
    bot.send_message(message.from_user.id, "Вибери назву продукту:", reply_markup=markup)


@bot.message_handler(commands=['site', 'website'])
def main(message):
    markup = types.InlineKeyboardMarkup()
    btn_url = types.InlineKeyboardButton(text='Перейти на сторінку', url='https://www.youtube.com/watch?v=dQw4w9WgXcQ')
    markup.add(btn_url)
    bot.send_message(message.chat.id, 'Натисніть на кнопку, щоб перейти на сторінку', reply_markup=markup)


@bot.message_handler(commands=['help'], content_types=['text', 'document', 'audio'])
def main(message):
    bot.send_message(message.from_user.id, f"Список команд:\n /start - Вибрати продукт \n /website - Веб-сторінка")


@bot.message_handler(content_types=['text'])
def get_Kasha(message):
    match message.text:
        case '🫕 Гречана':
            msg = bot.send_message(message.from_user.id, "Введіть кількість грам")
            bot.register_next_step_handler(msg, process_multy2)
        case '🍚 Рис':
            msg = bot.send_message(message.from_user.id, "Введіть кількість грам")
            bot.register_next_step_handler(msg, process_multy2)
        case '🥣 Вівсяна':
            msg = bot.send_message(message.from_user.id, "Введіть кількість грам")
            bot.register_next_step_handler(msg, process_multy25)
        case '🍝 Макарони':
            msg = bot.send_message(message.from_user.id, "Введіть кількість грам")
            bot.register_next_step_handler(msg, process_multy10)
        case '🌽 Кукурудзяна':
            msg = bot.send_message(message.from_user.id, "Введіть кількість грам")
            bot.register_next_step_handler(msg, process_multy3)
        case '🍲 Перлова':
            msg = bot.send_message(message.from_user.id, "Введіть кількість грам")
            bot.register_next_step_handler(msg, process_multy3)


def process_multy2(message):
    try:
        quantity = int(message.text)
        glass_amount = round(quantity / 300, 1)
        water_amount = round(glass_amount * 2, 1)
        bot.send_message(message.chat.id, f"Для {glass_amount} стаканів каши потрібно {water_amount} стаканів води.")
    except ValueError:
        bot.send_message(message.chat.id, "Будь ласка, введіть число.")


def process_multy25(message):
    try:
        quantity = int(message.text)
        glass_amount = round(quantity / 300, 1)
        water_amount = round(glass_amount * 2.5, 1)
        bot.send_message(message.chat.id, f"Для {glass_amount} стаканів каши потрібно {water_amount} стаканів води.")
    except ValueError:
        bot.send_message(message.chat.id, "Будь ласка, введіть число.")


def process_multy3(message):
    try:
        quantity = int(message.text)
        glass_amount = round(quantity / 300, 1)
        water_amount = round(glass_amount * 3, 1)
        bot.send_message(message.chat.id, f"Для {glass_amount} стаканів каши потрібно {water_amount} стаканів води.")
    except ValueError:
        bot.send_message(message.chat.id, "Будь ласка, введіть число.")


def process_multy10(message):
    try:
        quantity = int(message.text)
        water_amount = round(quantity * 10, 1)
        bot.send_message(message.chat.id, f"Для {quantity} грамів макаронів потрібно {water_amount} мл води.")
    except ValueError:
        bot.send_message(message.chat.id, "Будь ласка, введіть число.")


bot.infinity_polling()
