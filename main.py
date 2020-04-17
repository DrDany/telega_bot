import telebot
import settings
import os
from telega_bot.qiwi import qiwi


TOKEN = settings.TOKKEN

bot = telebot.TeleBot(TOKEN)

print(bot.get_me())


def log(message, answer):
    print("\n-----")
    from datetime import datetime
    print(datetime.now())
    # print("Сообщение от (0) (1). (id = (2)) \n Текст - (3)".format(message.from_user.first_name,
    #                                                                message.from_user.last_name,
    #                                                                str(message.from_user.id),
    #                                                                message.text))
    print('User ID =', message.from_user.id)
    print('User name =', message.from_user.first_name)
    print(answer)


@bot.message_handler(commands=['help'])
def send_message(message):
    answer = "Пиши @Scofield73"
    log(message, answer)
    bot.send_message(message.chat.id, "Пиши @Scofield73")


@bot.message_handler(commands=['start'])
def handler_start(message):
    answer = "Билеты, Профиль, Пополнить счет, Информация, Поддержка"
    log(message, answer)
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_markup.row('Билеты', 'Профиль')
    user_markup.row('Пополнить счет', 'Информация', 'Поддержка')
    bot.send_message(message.from_user.id, "Привет!", reply_markup=user_markup)




@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == "Информация":
        answer = "Гони сотку, пидр"
        log(message, answer)
        bot.send_message(message.from_user.id, "Гони сотку, пидр")
    elif message.text == "Пополнить счет":
        answer = "QIWI кошелек 89180000000, при переводе в комментарии обязательно укажи свой id,иначе,деньги не зачислятся!"
        log(message, answer)
        bot.send_message(message.from_user.id, "QIWI кошелек 89180000000, при переводе в комментарии обязательно укажи свой id,иначе,деньги не зачислятся!")
    elif message.text == "Поддержка":
        answer = "Пиши @Scofield73"
        log(message, answer)
        bot.send_message(message.from_user.id, "Пиши @Scofield73")
    elif message.text == "Билеты":
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row('50', '100', '200')
        user_markup.row('300', '500', 'Назад')
        bot.send_message(message.from_user.id, "Какой билет?", reply_markup=user_markup)
    elif message.text == "Назад":
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row('Билеты', 'Профиль')
        user_markup.row('Пополнить счет', 'Информация', 'Поддержка')
        bot.send_message(message.from_user.id, "Привет!", reply_markup=user_markup)
    elif message.text == "Профиль":
        answer = " Профиль id:\nВаш баланс:\nВсего купленных билетов"
        log(message, answer)
        str = "Профиль id: %s \nВаш баланс:\nВсего купленных билетов" % message.from_user.id
        bot.send_message(message.from_user.id, str)
    else:
        bot.send_message(message.from_user.id, "Нет такой команды.")


balance = qiwi.get_payment(1)



# print(message.chat_id)
bot.polling(none_stop=True, interval=0)