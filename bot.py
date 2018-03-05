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
randlist=['Шальная Императрица', 'Равен', 'Котейка', 'Артем', 'Возбужденный Самец', 'Писюк', 'Веган', 'Пйос', 'Большой Банан', 'Мявс', 'Клубничка', 'Гей Воробей', 'Енотик']
@bot.callback_query_handler(func=lambda call:True)
def inline(call):
    if call.data=='join':        
      try:
        if call.from_user.id not in info.lobby.game[call.message.chat.id]['players']:
              z=0
              for ids in info.lobby.game:
                  if call.from_user.id in info.lobby.game[ids]['players']:
                    z+=1    
              if z==0:
               if len(info.lobby.game[call.message.chat.id]['players'])<12:
                  info.lobby.game[call.message.chat.id]['players'].update(createuser(call.from_user.id, call.message.chat.id))
                  bot.send_message(call.message.chat.id, 'Аноним присоединился!')
                  info.lobby.alreadyplay.append(call.from_user.id)
               if len(info.lobby.game[call.message.chat.id]['players'])>11:
                bot.send_message(call.message.chat.id, 'Набор окончен!')
                begin(call.message.chat.id)
      except:
        pass
                                  


def del2(id):
    try:
      bot.send_message(id, '25 минут прошло! Вирт остановлен!')
      del info.lobby.game[id]
    except:
      pass

def delplayer(id, id2):
    del info.lobby.game[id]['players'][id2]
    info.lobby.game[id]['nicks'].remove(info.lobby.game[id]['players'][id2]['nick'])
            
def deleter(id):
  try:
    del info.lobby.game[id]
  except:
    pass
    
@bot.message_handler(commands=['stop'])
def s(m):
  for ids in info.lobby.game:
    if m.from_user.id in info.lobby.game[ids]['players']:
        bot.send_message(ids, 'Аноним вышел!')
        t=threading.Timer(5, delplayer, args=[ids])
        t.start()

@bot.message_handler(commands=['lobby'])
def m(m):
    if m.chat.id not in info.lobby.game:
        t=threading.Timer(1500, del2, args=[m.chat.id])
        t.start()
        bot.send_message(441399484, 'Вирт начался где-то!')
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
    info.lobby.game[id]['nicks'].append(x)
    return x
        
        
def begin(id):
    for ids in info.lobby.game[id]['players']:
      try:
        bot.send_message(ids, 'Пишите сюда что то')
      except:
        bot.send_message(id, 'Какой то пидорас не открыл диалог с ботом!')
    
    
@bot.message_handler(content_types=['text'])
def h(m):
    for ids in info.lobby.game:
        if m.from_user.id in info.lobby.game[ids]['players']:
          if m.chat.id>0:
            try:
              bot.send_message(ids, info.lobby.game[ids]['players'][m.from_user.id]['name']+':\n'+m.text)
            except:
                pass
            

    
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



