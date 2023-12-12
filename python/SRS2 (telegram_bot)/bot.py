from telebot import *
import emoji

bot = telebot.TeleBot('6593889559:AAFEnaxI9L85QmLfyXmYOycnEzpXFpaeRTk', parse_mode=None)


@bot.message_handler(content_types=['text', 'document', 'audio'])
def get_text_messages(message):
    print("\n")
    print(message)
    print("\n")
    match message.text:
        case "/start":
            bot.send_message(message.from_user.id, f"Привет {message.from_user.first_name}!")
            markup = types.ReplyKeyboardMarkup()
            itembtna = types.KeyboardButton(emoji.emojize(':1st_place_medal: Я черный!'))
            itembtnv = types.KeyboardButton(emoji.emojize('v'))
            itembtnc = types.KeyboardButton(emoji.emojize('c'))
            itembtnd = types.KeyboardButton(emoji.emojize('c'))
            itembtne = types.KeyboardButton(emoji.emojize('c'))
            itembtnj = types.KeyboardButton(emoji.emojize('c'))
            markup.row(itembtna, itembtnv)
            markup.row(itembtnc, itembtnd)
            markup.row(itembtne, itembtnj)
            bot.send_message(message.from_user.id, "Choose one letter:", reply_markup=markup)


bot.infinity_polling()
