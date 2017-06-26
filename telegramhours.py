from telebot import types

def create_hours():
    markup = types.InlineKeyboardMarkup()
    row=[]
    dates= []
    foo = 0
    bar = ['00','30']
    for i in range(0,24):
        for j in range(0,len(bar)):
            dates.append('%s:%s'%(i ,bar[j]))
    i = 0
    for date in dates:
        i = i + 1 
        row.append(types.InlineKeyboardButton(date,callback_data="hour-%s"%(date)))
        if i%6 == 0:
            markup.row(*row)
            row = []
    return markup

