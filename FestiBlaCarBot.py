import FestiBlaCarDb
from tripjournal import TripJournal
import telebot
from telebot import types
import time
from telegramcalendar import create_calendar
import datetime
from telegramhours import create_hours
current_shown_dates={}

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
                options(cid)
            elif  m.text == 'get_all_trips':
                command_all_trips(cid)
            elif  m.text == 'get_all_users':
                command_all_users(cid)
            elif  m.text == '/start':
                options(cid)

            else:
                addTripData(cid,m.text)
        else:
            print(m.content_type)

def addTripData(cid,data):
    trip = None
    for tj in journals:
        if cid == tj.idTgm:
            trip = tj
    if trip != None:
        tj.input(data)
        if tj.out() == 'Fecha':
            get_calendar(cid)
        elif tj.out() == 'Hora':
            bot.send_message(cid, "------Please, choose a Hour-----", reply_markup=create_hours())
        else:
            bot.send_message( cid , tj.out())

        

def createTrip(cid):
    tj = TripJournal(cid)
    journals.append(tj)
    bot.send_message( cid , tj.out())

def insertTrip(cid):
    for tj in journals:
        if cid == tj.idTgm:
            trip = tj
    db.insert_full_trip(trip.fields[0],trip.fields[1],trip.fields[2],trip.fields[3],trip.fields[4],trip.fields[5],trip.idTgm)
    journals.remove(trip)    


def command_all_trips(cid): # Definimos una función que resuleva lo que necesitemos.
    print("%s"%(db.get_all_trips()))        
    bot.send_message( cid, "%s"%(db.get_all_trips()))

def command_all_users(cid): # Definimos una función que resuleva lo que necesitemos.
    print("%s"%(db.get_all_users()))
    bot.send_message( cid, "%s"%(db.get_all_users()))

def options(cid):
    markup = types.InlineKeyboardMarkup()
    btnCre = types.InlineKeyboardButton('Create',callback_data="create")
    btnVie = types.InlineKeyboardButton('Serach',callback_data="search")
        
    markup.add(btnCre, btnVie)
    bot.send_message(cid, '▲                   Select                     ▲', None, None, markup)


def get_calendar(cid):
    now =datetime.datetime.now() #Current date
    chat_id = cid
    date = (now.year,now.month)
    current_shown_dates[chat_id] = date #Saving the current date in a dict
    markup= create_calendar(now.year,now.month)
    bot.send_message(cid, "Please, choose a date", reply_markup=markup)


def next_month(call):
    chat_id = call.message.chat.id
    saved_date = current_shown_dates.get(chat_id)
    if(saved_date is not None):
        year,month = saved_date
        month+=1
        if month>12:
            month=1
            year+=1
        date = (year,month)
        current_shown_dates[chat_id] = date
        markup= create_calendar(year,month)
        bot.edit_message_text("Please, choose a date", call.from_user.id, call.message.message_id, reply_markup=markup)
        bot.answer_callback_query(call.id, text="")
    else:
        pass

def previous_month(call):
    chat_id = call.message.chat.id
    saved_date = current_shown_dates.get(chat_id)
    if(saved_date is not None):
        year,month = saved_date
        month-=1
        if month<1:
            month=12
            year-=1
        date = (year,month)
        current_shown_dates[chat_id] = date
        markup= create_calendar(year,month)
        bot.edit_message_text("Please, choose a date", call.from_user.id, call.message.message_id, reply_markup=markup)
        bot.answer_callback_query(call.id, text="")
    else:
        pass


def get_day(call):
    chat_id = call.message.chat.id
    saved_date = current_shown_dates.get(chat_id)
    if(saved_date is not None):
        day=call.data[13:]
        date = datetime.date(int(saved_date[0]),int(saved_date[1]),int(day))
        addTripData(chat_id, str(date))
        bot.answer_callback_query(call.id, text="")
    else:
        pass

def get_hour(call):
    chat_id = call.message.chat.id
    day=call.data[5:]
    addTripData(chat_id, str(day))
    bot.answer_callback_query(call.id, text="")

@bot.callback_query_handler(func=lambda call: True)
def iq_callback(query):
    data = query.data
    print(data)
    if data.startswith('create'):
        bot.answer_callback_query(query.id)
        createTrip(query.message.chat.id)
    
    if data == 'next-month':
        next_month(query)
    if data == 'previous-month':
        previous_month(query)
    if data[0:13] == 'calendar-day-':
        get_day(query)
    if data.startswith('hour-'):
        get_hour(query)

bot.set_update_listener(listener)
bot.polling(none_stop=True)



