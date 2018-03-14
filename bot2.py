# -*- coding: utf-8 -*-
import redis
import os
import telebot
import math
import random
import threading
import info
import test
import pprint
from pymongo import MongoClient
from telebot import types
from emoji import emojize
token = os.environ['TELEGRAM_TOKEN']
bot = telebot.TeleBot(token)

client = MongoClient('localhost', 27017)
db = client.database
collection = db.collection

size={'x':445}

sizes=db.sizes
sizeid=sizes.insert_one(size).inserted_id
pprint.pprint(sizes.find_one())


