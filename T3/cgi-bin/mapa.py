# !/usr/bin/python3
# -*- coding: utf-8 -*-

print("Content-type:  application/json")
print("")

import cgi
import cgitb

cgitb.enable()

from db import DB
import sys
import codecs
import json

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
db = DB('localhost', 'root', '', 'tarea2')

comuna_fotos  = db.get_comuna_fotos()

with open("JSON/chile.json", "r", encoding="utf-8") as file:
    jason = file.read()
    chile =  json.loads(jason)

dic = {}
for t in chile:
    dic[t['name']] = [float(t['lat']), float(t['lng'])]

location = []
for comuna in comuna_fotos:
    try:
        ncomuna = comuna[0]
        location.append([comuna[2], dic[ncomuna], comuna[1]])
    except:
        pass
y = json.dumps(location, ensure_ascii=False)
print(y)