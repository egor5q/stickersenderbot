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
penis=0
spisok=['Ппц', 'Мда.', 'Дороу']
spisok2=[]
@bot.message_handler(commands=['chlen'])
def c(m):
    bot.send_message(m.chat.id, 'Да да да, я работаю, отъебитесь')

@bot.message_handler(commands=['sasat'])
def sasat(m):
    bot.send_message(m.chat.id, 'О, вы выбрали пункт "сасат"! Вы сасали '+str(random.randint(1, 100))+' членов!')

@bot.message_handler(commands=['penis'])
def penis(m):
    global penis
    penis+=0.1
    bot.send_message(m.chat.id, 'Ура! Вы увеличили мой пенис! Теперь он '+str(penis)+ 'см!')
    
def pisuk():
    global pisuks
    pisuks=0
          
@bot.message_handler(content_types=['text'])
def textm(m):
    global pisuks
    global alr
    p=m.text.lower()
    if 'или' in p:
        n=0
        ili=0
        while n<len(p):
            try:
              if p[n]=='и' and p[n+1]=='л' and p[n+2]=='и':
                ili+=1
            except:
                pass
            n+=1
        print(str(ili))
        a=p.split('или')
        dd=0
        g=0
        
        try:
         while g< len(a):
          j=len(a[g])
          if g<len(a) and g>0:       
            if a[g][0]==' ' and a[g][j-1]==' ':
                dd=1
          elif g==0:
            if a[g][j-1]==' ':
                dd=1
          elif g==len(a)-1:
            if a[g][0]==' ':
                dd=1
          g+=1
        except:
            pass
        
            
        print (a)        
        if ili>0:
         if dd==1:
          try:
            rd=random.randint(0,ili)
            count=0
            slovar=a[rd]
            for i in slovar:
                count+=1
            if slovar[count-1]=='?':
              slovar=slovar[:(count-1)]
              print(slovar)
            if slovar[0]=='я' or slovar[0]=='Я':
              slovar=slovar[1:]
              print(slovar)
            slovar=slovar.capitalize()
            print(slovar)
            bot.send_message(m.chat.id, slovar)
          except:
            pass
    if 'пасюк пидр' in p or 'писюк пидр' in p or 'пасюк пидор' in p or 'писюк пидр' in p:
        bot.send_message(m.chat.id, 'Нахуй иди')
        alr=1
    if pisuks==1:
        print('1')
        if 'п' in p and 'и' in p and 'д' in p and 'р' in p and len(p)<250:
            for x in p:
                if x not in spisok2:
                    spisok2.append(x)
            if len(spisok2)<15:                
              print('2')
              if alr==0:
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
        t=threading.Timer(4, pisuk)
        t.start()
        print('3')
    if 'п' in p and 'и' in p and 'ю' in p and 'к' in p and 'д' in p and len(p)<250:
     if 'p' not in p and 'c' not in p and 'i' not in p and 'a' not in p and 'd' not in p and 'u' not in p:
      if 'р' in p:
        if 'с' in p:
           if pisuks==1:
              for x in p:
                if x not in spisok2:
                 spisok2.append(x)
              if len(spisok2)<18:           
                if alr==0:
                  bot.send_message(m.chat.id, 'Нахуй иди')
                  pisuks=0
                  alr=1
                
                     
     else:
        if len(spisok2)<15:
          bot.send_message(m.chat.id, 'Нахуй иди')
    elif 'p' in p and 'a' in p and 's' in p and 'u' in p and 'k' in p and 'i' in p and 'd' in p and 'r' in p:
        for x in p:
                if x not in spisok2:
                 spisok2.append(x)
        if len(spisok2)<15: 
         if alr==0:
          bot.send_message(m.chat.id, 'nahui idi')
          alr=1
    spisok2.clear()
    alr=0
        
        
        
if __name__ == '__main__':
  bot.polling(none_stop=True)



