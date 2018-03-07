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

spisok=['Пиздец', 'Бляяяяяя', 'Дороу', 'Кто будет сосать?']

@bot.message_handler(commands=['chlen'])
def c(m):
    bot.send_message(m.chat.id, 'Да да да, я работаю, отъебитесь')

@bot.message_handler(commands=['sasat'])
def sasat(m):
    bot.send_message(m.chat.id, 'О, вы выбрали пункт "сасат"! Вы сасали '+str(random.randint(1, 1000))+' членов!')
       
        
@bot.message_handler(content_types=['text'])
def textm(m):
    z=random.randint(1, 100)
    if z==1:
        speach=random.choice(spisok)
        bot.send_message(m.chat.id, speach)
    x=m.text.lower()
    if 'писюк пид' in x or 'пасюк пид' in x:
        bot.send_message(m.chat.id, 'Нахуй иди')
    elif 'вирт' in x:
        bot.send_message(m.chat.id, 'Я тоже хочу повиртить!')
    elif 'хуй' in x:
        bot.send_message(m.chat.id, 'ВЫ СКАЗАЛИ "ХУЙ"!')
        
        
        
if __name__ == '__main__':
  bot.polling(none_stop=True)



