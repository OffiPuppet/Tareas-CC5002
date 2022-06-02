# !/usr/bin/python3
# -*- coding: utf-8 -*-

import cgi
import cgitb
from db import DB
import sys
import codecs
import json
cgitb.enable()

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach()) # Para que funcione el UTF-8

db = DB('localhost', 'root', '', 'tarea2')

tipos = db.get_actividad_por_date()
fechas = [str(p[0]) for p in tipos]
numero = [p[1] for p in tipos]
data = [{'x': fechas, 'y': numero, 'type':'line'}]
y = json.dumps(data, ensure_ascii=False).encode('utf8').decode('utf8')
print(y)