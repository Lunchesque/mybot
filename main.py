import telebot


bot = telebot.TeleBot(token="480284355:AAFr3T9YIPNj-kATXZUR5xblQri64FSw9aY")


#bot.send_message(225191458, "test")

"""
upd = bot.get_updates()
#print(upd)

last_upd = upd[-1]

msg_from_user = last_upd.message
print(msg_from_user)
"""

print(bot.get_me())



def log(message, answer):
    print("\n ------------------")
    from datetime import datetime
    print(datetime.now())
    print("Message from [0] [1]. (id = [2]) \n Text - [3]".format(message.from_user.first_name,
                                                                  message.from_user.last_name,
                                                                  str(message.from_user.id),
                                                                  message.text))
    print(answer)



@bot.message_handler(commands=['help'])
def hendle_text(message):
    bot.send_message(message.chat.id, """Запрос "А" - ответ "Б"
Запрос "Б" - ответ "С"
Запрос 1 - ответ "Its 1 or 2"
Запрос 2 - ответ "Its 1 or 2""")

@bot.message_handler(commands=['location'])
def hendle_text(message):
    bot.send_message(message.chat.id, "Minsk")

@bot.message_handler(content_types=["text"])
def hendle_text(message):
    answer = "wut?"
    if message.text == "а" or message.text == "А":
        answer = "Б"
        log(message, answer)
        bot.send_message(message.chat.id, answer)

    elif message.text == "б" or message.text == "Б":
        answer = "В"
        bot.send_message(message.chat.id, answer)
        log(message, answer)

    elif message.text == "1" or message.text == "2":
        answer = "its 1 or 2"
        bot.send_message(message.chat.id, answer)
        log(message, answer)

    else:
        bot.send_message(message.chat.id, answer)
        log(message, answer)

bot.polling(none_stop=True, interval=0)
