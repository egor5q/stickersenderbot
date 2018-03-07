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
pisuks=0
alr=0
spisok=['Пиздец', 'Бляяяяяя', 'Дороу', 'Кто будет сосать?']
spisok2=[]
@bot.message_handler(commands=['chlen'])
def c(m):
    bot.send_message(m.chat.id, 'Да да да, я работаю, отъебитесь')

@bot.message_handler(commands=['sasat'])
def sasat(m):
    bot.send_message(m.chat.id, 'О, вы выбрали пункт "сасат"! Вы сасали '+str(random.randint(1, 1000))+' членов!')

def pisuk():
    global pisuks
    pisuks=0
          
@bot.message_handler(content_types=['text'])
def textm(m):
    global pisuks
    global alr
    p=m.text.lower()
    if 'или' in p:
        a=p.split('и')
        print (a)
    if pisuks==1:
        print('1')
        if 'п' in p and 'и' in p and 'д' in p and 'р' in p and len(p)<250:
            for x in p:
                if x not in spisok2:
                    spisok2.append(x)
            if len(spisok2)<20:                
              print('2')
              bot.send_message(m.chat.id, 'Нахуй иди')
              pisuks=0
              alr=1
            spisok2.clear()
    z=random.randint(1, 100)
    if z==1:
        speach=random.choice(spisok)
        bot.send_message(m.chat.id, speach)
    if 'п' in p and 'с' in p and 'ю' in p and 'к' in p and len(p)<250:
        pisuks=1
        print('3')
    if 'п' in p and 'и' in p and 'ю' in p and 'к' in p and 'д' in p and len(p)<250:
     if 'p' not in p and 'c' not in p and 'i' not in p and 'a' not in p and 'd' not in p and 'u' not in p:
      if 'р' in p:
        if 'с' in p:
           if pisuks==1:
              for x in p:
                if x not in spisok2:
                 spisok2.append(x)
              if len(spisok2)<20:           
                if alr==0:
                  bot.send_message(m.chat.id, 'Нахуй иди')
                  pisuks=0
                else:
                  alr=0    
     else:
        bot.send_message(m.chat.id, 'Английская раскладка! Идите нахуй.')
    if 'p' in p and 'a' in p and 's' in p and 'u' in p and 'k' in p and 'i' in p and 'd' in p and 'r' in p:
      bot.send_message(m.chat.id, 'nahui idi')
    spisok2.clear()
        
        
        
if __name__ == '__main__':
  bot.polling(none_stop=True)



