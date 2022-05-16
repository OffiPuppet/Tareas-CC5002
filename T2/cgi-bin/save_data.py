# !/usr/bin/python3
# -*- coding: utf-8 -*-
import cgi
import os
import re
import sys
from db import DB

print("Content-type: text/html; charset=UTF-8")
print()

db = DB("localhost", "root", "", "tarea2")
form = cgi.FieldStorage()

MAX_FILE_SIZE = 10 * 1000000  # 10 MB

utf8stdout = open(1, "w", encoding="utf-8", closefd=False)

def check(regex, value):
    return re.fullmatch(regex, value)

# Str que suma todas las alertas de error
errores = "<ul>Su formulario tiene errores:</ul>"
largo_inicial = len(errores)

rrss = form.getvalue("contactar-por")
Otro = form.getvalue("Otro")
comuna = form.getvalue("comuna")
sector = form.getvalue("sector")
nombre = form.getvalue("nombre")
email = form.getvalue("email")
celular = form.getvalue("celular")
identificador = form.getvalue("inputcontacto")
#print(identificador)
inicio = form.getvalue("dia-hora-inicio")
termino = form.getvalue("dia-hora-termino")
descripcion = form.getvalue("descripcion-evento")
tema = form.getvalue("tema")
fotos = form["foto-actividad"]

# TEMA :========================
if 'tema' not in form:
    errores += '<li>Por favor, seleccione un TEMA del menú.</li>'
else:
    regex4 = '^\d+$'
    if tema != 'otro' and not (check(regex4, tema)):
        errores += '<li>Ha seleccionado un tema no permitido.</li>'
    if tema == 'otro':
        if 'nuevo-tema' not in form:
            errores += '<li>Debe ingresar un nuevo tema .</li>'
        else:
            Otro_tema = form.getvalue('inputTema')
            if len(Otro_tema) < 3 or len(Otro_tema) > 15:
                errores += '<li>Debe ingresar un nuevo tema de tamaño entre 3 y 15 caracteres.</li>'

if tema == 'Otro':
    db.guardar_tema(Otro_tema)
    nuevo_temaID = db.get_temaID(Otro_tema)
    tema = nuevo_temaID[0][0]

### A continuación hay dos diccionarios con las tuplas para facilitar el llamado posterior

if not (type(fotos) == list):
    fotos = [fotos]

region = form.getvalue("region")
region_id = db.get_region_id(region)
region_name = db.get_region_name(region)
#print(region_name)
comuna_id = db.get_comuna_id(comuna, region_id)
comuna_name = db.get_comuna_data(comuna_id)
#print(comuna_name)
tema_nombre = db.get_temas(tema)
#print(tema_nombre)

actividad = {'comuna': comuna_id,
             'sector': sector,
             'nombre': nombre,
             'email': email,
             'celular': celular,
             'dia-hora-inicio': inicio,
             'dia-hora-termino': termino,
             'descripcion': descripcion,
             'tema': tema
             }

act = db.guardar_actividad(actividad)

redes_sociales = {'nombre': rrss,
                'id': identificador,
                'id_act': act
                }
db.guardar_contacto(redes_sociales)

data = (actividad, redes_sociales, fotos)
#print(data)
db.save_data(data)  # ejecutamos consulta para guardar la actividad
listo = """
            <h1>¡Tu formulario ha sido recibido!</h1>
            <h2>Gracias por agregar tu actividad.</h2>
"""

print(utf8stdout.write(listo))