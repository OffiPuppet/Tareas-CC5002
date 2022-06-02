# !/usr/bin/python3
# -*- coding: utf-8 -*- 
import cgi
import cgitb
import json
from db import DB

cgitb.enable()
utf8stdout = open(1, 'w', encoding='utf-8', closefd=False)

db = DB("localhost","root", "", "tarea2")

data_grafico_1 = db.get_grafico1()
data_grafico_2 = db.get_grafico2()
data_grafico_31, data_grafico_32, data_grafico_33 = db.get_grafico3()


grafico_json = {
    "grafico_1": data_grafico_1,
    "grafico_2": data_grafico_2,
    "grafico_3": {
        "grafico_3_1": data_grafico_31,
        "grafico_3_2": data_grafico_32,
        "grafico_3_3": data_grafico_33
    }
}

grafico_json = json.dumps(grafico_json)

utf8stdout.write(grafico_json)