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
print('Content-type: text/html; charset=UTF-8')
print("")

informacion = {}
cantidad = db.get_datos_g1()
fecha_inicial = cantidad[0][1].strftime("%d-%m-%Y")
datos,fecha_actual = [],''
k = -1
for i in cantidad:
    fecha = i[1].strftime("%d-%m-%Y")
    if fecha == fecha_actual:
        datos[k][1] += 1
    else:
        datos.append([str(fecha),1])
        k +=1
        fecha_actual = fecha
informacion[0] = datos
print(json.dumps(informacion))