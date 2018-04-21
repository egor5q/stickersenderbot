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


client=MongoClient('mongodb://egor5q:123@db-shard-00-00-fej0s.mongodb.net:27017,db-shard-00-01-fej0s.mongodb.net:27017,db-shard-00-02-fej0s.mongodb.net:27017/test?ssl=true&replicaSet=DB-shard-0&authSource=admin')
db=client.db1
collection=db.coll



@bot.message_handler(content_types=['text'])
def textm(m):
    x=0
    for slovo in mat:
        if slovo.lower() in m.text:
            x=1
    if x==1:
        z=random.randint(0, len(stickerid)-1)
        bot.send_sticker(m.chat.id, stickerid[z])
    


if __name__ == '__main__':
  bot.polling(none_stop=True)



