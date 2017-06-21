import FestiBlaCarDb
from tripjournal import TripJournal
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
timestamp = int(time.time())
journals = []
db = FestiBlaCarDb.Db()
db.create_db()
def listener(messages): 
    for m in messages: 

        if m.content_type == 'text' and m.date > timestamp:
            cid = m.chat.id
            username = m.chat.username
            db.insert_user(cid,username)
            if m.text == 'New':
                createTrip(cid)
            elif m.text == 'End':
                insertTrip(cid)
            elif  m.text == 'get_all_trips':
                command_all_trips(cid)
            elif  m.text == 'get_all_users':
                command_all_users(cid)
            else:
                addTripData(cid,m.text)

def addTripData(cid,data):
    trip = None
    for tj in journals:
        if cid == tj.idTgm:
            trip = tj
    if trip != None:
        tj.input(data)
        bot.send_message( cid , tj.out() )

def createTrip(cid):
    tj = TripJournal(cid)
    journals.append(tj)
    bot.send_message( cid , tj.out())

def insertTrip(cid):
    for tj in journals:
        if cid == tj.idTgm:
            trip = tj
    db.insert_full_trip(trip.fields[0],trip.fields[1],trip.fields[2],trip.fields[4],trip.idTgm)
    journals.remove(trip)    


def command_all_trips(cid): # Definimos una función que resuleva lo que necesitemos.
    print("%s"%(db.get_all_trips()))        
    bot.send_message( cid, "%s"%(db.get_all_trips()))

def command_all_users(cid): # Definimos una función que resuleva lo que necesitemos.
    print("%s"%(db.get_all_users()))
    bot.send_message( cid, "%s"%(db.get_all_users()))
bot.set_update_listener(listener)
bot.polling(none_stop=True)



