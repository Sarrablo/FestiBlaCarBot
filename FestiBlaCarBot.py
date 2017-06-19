import FestiBlaCarDb
import telebot
from telebot import types
import time


f  = open('credentials','r')
token = f.read()
f.close()
print(token)
TOKEN = token 
bot = telebot.TeleBot('430791351:AAHC-M4rgsPLxfpeASMj3sz4Zy0bSMSgXdU') # Creamos el objeto de nuestro bot.
print (bot.get_me())


