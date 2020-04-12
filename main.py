import telebot
import settings

TOKEN = settings.TOKKEN

bot = telebot.TeleBot(TOKEN)



@bot.message_handler(commands=['help'])
def send_message(message):
    bot.send_message(message.chat.id, "Спрашивай че надо")


@bot.message_handler(commands=['start'])
def handler_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_markup.row('/start', '/stop')
    user_markup.row('фото', 'audio', 'docs')
    user_markup.row('sticker', 'video', 'voice', 'local')
    bot.send_message(message.from_user.id, "Даааароу", reply_markup=user_markup)


@bot.message_handler(commands=['stop'])
def handler_start(message):
    hide_markup = telebot.types.ReplyKeyboardRemove()
    bot.send_message(message.from_user.id, "...", reply_markup=hide_markup)


@bot.message_handler(content_types=['text'])
def send_message(message):
    if message.text == '100':
        bot.send_message(message.chat.id, "Гони сотку, пидр")


bot.polling(none_stop=True, interval=0)
