# -*- coding: utf-8 -*-
import redis
import os
import telebot
import math
import random
import threading
import info
import test
from telebot import types
from emoji import emojize
token = os.environ['TELEGRAM_TOKEN']
bot = telebot.TeleBot(token)

@bot.callback_query_handler(func=lambda call:True)
def inline(call):
    if call.data=='join':
        if call.from_user.id not in info.lobby.game[call.chat.id]['players']:
            pass





@bot.message_handler(commands=['lobby'])
def m(m):
    if m.chat.id not in info.lobby.game:
        Keyboard=Types.InlineKeyboardMarkup()
        info.lobby.game.update(createroom(m.chat.id))
        Keyboard.add('Тык', callback_data='join')
        msg=bot.send_message(m.chat.id, 'Начинаем! жмите на кнопку, чтобы присоединиться', reply_markup=Keyboard)
    else:
        pass



def createroom(id)
return{id:{
    'player1':None,
    'player2':None
}
    
        
        
if __name__ == '__main__':
  bot.polling(none_stop=True)



