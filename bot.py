# -*- coding: utf-8 -*-
import redis
import os
import telebot
import math
import random
import threading
from pymongo import MongoClient
from telebot import types
from emoji import emojize
token = os.environ['TELEGRAM_TOKEN']
bot = telebot.TeleBot(token)

chance=100

mat=['хуй', 'пизда', 'залупа', 'хер', 'пидор', 'бля', 'ебать', 'пиздя', 'выебон', 'ебал', 'ебло', 'хуепутало', 'заебись', 'ебал', 
     'ёбаный', 'пёзда', 'хуе']
stickerid=['CAADAgAD5QUAAnwFBxtu71sj1snukAI',
'CAADAgADLQADtA_ZFbR9r9ENWA_UAg',
'CAADAgADDwEAAjF_Eg1uXf7aM22nNgI',
'CAADAgADTwEAAjeEMAAB2Uln8bCZzR8C',
'CAADAgADYAADKcn5BgqmFb1yGuNYAg',
'CAADAgADbQMAAhXEzBprkstMCAxugwI',
'CAADAgADAQADU5BSFDBWDyBqwd5xAg',
'CAADAgADLAoAAr_cXAVGFHO8XO7BaAI',
'CAADBAADMgMAAjW7NgABlVCQJLpuDZIC',
'CAADBAADFQAD19F7AAGZz932SvtNHAI',
'CAADAgADgwEAAvXIwgYj685XCvmRswI',
'CAADBAADNgEAAnBt9gdGtfpzbERPJQI'
          ]




@bot.message_handler(commands=['setchance'])
def getadm(m):
     global chance
     if m.chat.id<0:
          x=bot.get_chat_administrators(m.chat.id)
          for z in x:
             if m.from_user.id==z:
               massiv=m.text.split('/setchance')
               try:
                    int(massiv[1])
                    chance=massiv[1]
                    bot.send_message(m.chat.id, 'Вы успешно изменили вероятность отправки стикера после мата на '+str(massiv[1])+'% !')
               except:
                    bot.send_message(m.chat.id, 'Неверный формат. Используйте следующий пример:\n/setchance *60*', parse_mode='markdown')
             else:
                    bot.send_message(m.chat.id, 'Только администраторы чата могут использовать эту команду!')
     else:
          bot.send_message(m.chat.id, 'Эту команду можно использовать только в группе!')


@bot.message_handler(content_types=['text'])
def textm(m):
  global chance
  a=random.randint(0, 100)
  if a<=chance:
    x=0
    for slovo in mat:
        if slovo.lower() in m.text.lower():
            x=1
    if x==1:
        z=random.randint(0, len(stickerid)-1)
        bot.send_sticker(m.chat.id, stickerid[z])
    


if __name__ == '__main__':
  bot.polling(none_stop=True)



