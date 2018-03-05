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
            if len(info.lobby.game[call.chat.id]['players'])<2:
              info.lobby.game[call.chat.id]['players'].update(createuser(call.from_user.id))
              bot.send_message(call.chat.id, 'Аноним присоединился!')
              if len(info.lobby.game[call.chat.id]['players'])>1:
                bot.send_message(call.chat.id, 'Поехали')
                begin(id)
            else:
                pass





@bot.message_handler(commands=['lobby'])
def m(m):
    if m.chat.id not in info.lobby.game:
        Keyboard=types.InlineKeyboardMarkup()
        info.lobby.game.update(createroom(m.chat.id))
        Keyboard.add(types.InlineKeyboardButton(text='Тык', callback_data='join'))
        msg=bot.send_message(m.chat.id, 'Начинаем! жмите на кнопку, чтобы присоединиться', reply_markup=Keyboard)
    else:
        pass


def begin(id):
    for id in info.lobby.game[id]['players']:
        bot.send_message(id, 'Пишите сюда что то')
    
    
@bot.message_handler(content_types=['text'])
def h(m):
    for ids in info.lobby.game:
        if m.from_user.id in info.lobby.game[ids]['players']:
            bot.send_message(ids, 'Аноним:\n'+m.text)

    
def createroom(id):
  return{id:{
    'players':{
    }
     }
      }   
        
def createuser(id):
    return{id:{
           'name':'Аноним'
          }
          }
       
       
       
       
if __name__ == '__main__':
  bot.polling(none_stop=True)



