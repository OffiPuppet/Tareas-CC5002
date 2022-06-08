# !/usr/bin/python3
# -*- coding: utf-8 -*-
print("Content-type:application/json")

import cgi
import cgitb
from db import DB
import sys
import codecs
import json
from datetime import date, datetime
cgitb.enable()

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

db = DB('localhost', 'root', '', 'tarea2')
print('Content-type: text/html; charset=UTF-8')
print("")

dates = db.get_month_hour()
months = []
mañana = {}
mediodia = {}
tarde = {}

t_6 = datetime.strptime('06:00', '%H:%M').time()
t_11 = datetime.strptime('11:00', '%H:%M').time()
t_15 = datetime.strptime('15:00', '%H:%M').time()

for pair in dates:
    if pair[0] not in months:
        months.append(pair[0])
        mañana[pair[0]] = 0
        mediodia[pair[0]] = 0
        tarde[pair[0]] = 0
    hora = datetime.strptime(pair[1], '%H:%M').time()
    
    if hora>=t_6 and hora<t_11:
        mañana[pair[0]]+=1

    elif hora>=t_11 and hora<t_15:
        mediodia[pair[0]]+=1
    
    else:
        tarde[pair[0]]+=1

months = [datetime.strftime(datetime.strptime(m, "%Y-%m"),'%B %Y') for m in months]
bar_mañana = {'x':months, 'y':list(mañana.values()),
 'name': 'Actividades que inician por la mañana'}

bar_mediodia = {'x':months, 'y':list(mediodia.values()),
 'name': 'Actividades que inician al mediodia'}

bar_tarde = {'x':months, 'y':list(tarde.values()),
 'name': 'Actividades que inician en la tarde'}

data = [bar_mañana, bar_mediodia, bar_tarde]
y = json.dumps(data, ensure_ascii=False).encode('utf8').decode('utf8')
print(y)