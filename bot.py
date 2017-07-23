# -*- coding: utf-8 -*-
import config
import telebot

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['spam'])
def game(message):
    command = message.text
    params = command.split( )
    if len(params) < 3:
        bot.send_message(message.chat.id, 'Wrong number of parameters')
    else:
        try:
            number = int(params[-1])
            message_to_send = params[1]
            for i in range(2, len(params) - 1):
                message_to_send += " " + params[i]
            for x in range(number):
                bot.send_message(message.chat.id, message_to_send)
        except ValueError:
            bot.send_message(message.chat.id, 'Last parameter should be integer')

if __name__ == '__main__':
    bot.polling(none_stop=True)
