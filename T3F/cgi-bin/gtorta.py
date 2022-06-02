# !/usr/bin/python3
# -*- coding: utf-8 -*-

import cgi
import cgitb
import sys
from db import DB
import codecs
import json
cgitb.enable()

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach()) # Pa' que funque UTF-8

db = DB('localhost', 'root', '', 'tarea2')

tipos = db.get_actividad_por_tema()
tipos1 = [p[1] for p in tipos]
valores = [p[0] for p in tipos]
data = [{'values': valores, 'labels': tipos1, 'type':'pie'}]
y = json.dumps(data, ensure_ascii=False).encode('utf8').decode('utf8')
print(y)