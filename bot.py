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
randlist=['Залупич', 'Равен', 'Котейка', 'Артем', 'Резко Пахнущая Пизда', 'Писюк', 'Веган', 'Пйос', 'Недотраханный Чечен', 'Большой Банан']
@bot.callback_query_handler(func=lambda call:True)
def inline(call):
    if call.data=='join':
      for chats in info.lobby.game:
        if call.from_user.id not in info.lobby.game[chats]['players']:
            if len(info.lobby.game[chats]['players'])<2:
              info.lobby.game[chats]['players'].update(createuser(call.from_user.id, chats))
              bot.send_message(chats, 'Аноним присоединился!')
              if len(info.lobby.game[chats]['players'])>1:
                bot.send_message(chats, 'Поехали')
                begin(chats)
            else:
                pass


def deleter(id):
    del info.lobby.game[id]
@bot.message_handler(commands=['stop'])
def s(m):
  for ids in info.lobby.game:
    if m.from_user.id in info.lobby.game[ids]['players']:
        bot.send_message(ids, 'Аноним остановил диалог!')
        t=threading.Timer(2, deleter, args=[ids])
        t.start()

@bot.message_handler(commands=['lobby'])
def m(m):
    if m.chat.id not in info.lobby.game:
        Keyboard=types.InlineKeyboardMarkup()
        info.lobby.game.update(createroom(m.chat.id))
        Keyboard.add(types.InlineKeyboardButton(text='Тык', callback_data='join'))
        msg=bot.send_message(m.chat.id, 'Начинаем! жмите на кнопку, чтобы присоединиться', reply_markup=Keyboard)
    else:
        pass

def namechoice(id):
    x=random.choice(randlist)
    while x in info.lobby.game[id]['nicks']:
        x=random.choice(randlist)
        
        
def begin(id):
    for ids in info.lobby.game[id]['players']:
        bot.send_message(ids, 'Пишите сюда что то')
    
    
@bot.message_handler(content_types=['text'])
def h(m):
    for ids in info.lobby.game:
        if m.from_user.id in info.lobby.game[ids]['players']:
          
            bot.send_message(ids, info.lobby.game[ids]['players'][m.from_user.id]['name']+':\n'+m.text)
          
            

    
def createroom(id):
  return{id:{
      'nicks':[],
    'players':{
    }
     }
      }   
        
def createuser(id, chatid):
    return{id:{
           'name':namechoice(chatid)
          }
          }
       
       
       
       
if __name__ == '__main__':
  bot.polling(none_stop=True)



