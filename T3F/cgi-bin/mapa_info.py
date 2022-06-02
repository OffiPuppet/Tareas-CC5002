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
form = cgi.FieldStorage()
id  = form.getvalue("id")
tema_id = form.getvalue("tema")

map_list = db.get_mapa_info(id)
map_list_dict = {}
id_revisados = []

def buscar_fotos(id, lista):
    fotos = []
    for data in lista:
        if data[0]==id:
            fotos.append(data[5])
        else:
            break
    return fotos

for i in range(len(map_list)):
    dato = map_list[i]
    if dato[1] not in map_list_dict:
        comuna = dato[1]
        map_list_dict[dato[1]] = []
    if dato[0] not in id_revisados:
        photos = buscar_fotos(dato[0], map_list[i:])
        map_list_dict[dato[1]].append([dato[0],*dato[2:5], photos])
        id_revisados.append(dato[0])

data =  map_list_dict
y = json.dumps(data, ensure_ascii=False).encode('utf8').decode('utf8')
inject = "<p>"+comuna+"</p>"
inject += "<table><tr><th>Enlace<th>dia-hora-inicio</th><th>Tema_nombre</th><th>Sector</th><th>Fotos</th></tr>"

for actividades in data[comuna]:
    nombre_tema = db.get_temas(actividades[2])
    inject += "<tr>"
    inject += "<td><a href='"+ "info_actividad.py?actividad_id="+str(actividades[0])+"'>Ver actividad</a></td>"
    inject += "<td>"+str(actividades[1])+"</td>"
    inject += "<td>"+str(nombre_tema)+"</td>"
    inject += "<td>"+str(actividades[3])+"</td>"
    inject += "<td><div class='container'>"
    fotos  = actividades[4]
    for foto in fotos:
        inject+= "<img class='table-image' src='../media/"+foto+"'"+"style='width: 80px; height: 60px;'>"
    inject += "</div></td>"
    inject += "</tr>"

inject += "</table>"

print(inject)