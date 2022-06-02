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

# ===================== REGION =====================
if 'region' not in form:
    errores += '<li>Por favor, seleccione una región del menú.</li>'

# ===================== COMUNA =====================
if 'comuna' not in form:
    errores += '<li>Por favor, seleccione una comuna del menú.</li>'

# ===================== NOMBRE DEL ORGANIZADOR =====================
if 'nombre' not in form:
    errores += '<li>Por favor, ingrese el nombre del(de la) organizador(a).</li>'
else:
    if nombre == '':
        errores += '<li>El ingreso de nombre es obligatorio.</li>'
    elif len(nombre) > 200:
        errores += '<li>Por favor, ingrese un nombre de largo menor a 200 caracteres.</li>'

# ===================== EMAIL =====================
if 'email' not in form:
    errores += '<li>Por favor, ingrese un email de contacto.</li>'
else:
    regex1 = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if email == '':
        errores += '<li>El ingreso de email es obligatorio.</li>'
    elif not (check(regex1, email)):
        errores += '<li>Por favor, ingrese un email en formato válido.</li>'

# ===================== DIA-HORA INICIO =====================
if 'dia-hora-inicio' not in form:
    errores += '<li>Por favor, ingrese una HORA DE INICIO.</li>'
else:
    regex3 = '[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1]) (2[0-3]|[01][0-9]):[0-5][0-9]'
    if inicio == '':
        errores += '<li>El ingreso de fecha inicial es obligatorio.</li>'
    if not (check(regex3, inicio)):
        errores += '<li>Por favor, ingrese un horario en formato correcto.</li>'

# ===================== TEMA =====================
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

# ===================== FOTOS =====================
def revisar_foto(imagen):
    alert = ''
    MAX_FILE_SIZE = 1000000
    blanks = 0
    if imagen.filename:
        tipo = imagen.type
        size = os.fstat(imagen.file.fileno()).st_size
        if not (tipo == 'image/jpeg' or tipo == 'image/png'):
            alert += '<li>Error, formato no válido.{}</li>'.format(tipo)
        if size > MAX_FILE_SIZE:
            alert += '<li>Error, archivo muy grande.</li>'
    else:
        blanks += 1

    return alert, blanks


if tema == 'Otro':
    db.guardar_tema(Otro_tema)
    nuevo_temaID = db.get_temaID(Otro_tema)
    tema = nuevo_temaID[0][0]

if 'foto-actividad' not in form:  # no hay input de foto en el form recibido
    errores += '<li>Por favor, carge al menos 1 IMAGEN.</li>'
else:
    if type(fotos) == list:  # significa que se cargo + de 1 archivo
        # print('es lista')  # test
        contador = 0
        for foto in fotos:
            resultado = revisar_foto(foto)
            errores += resultado[0]
            if resultado[1] > 0:
                contador += 1
                errores += f'<li>Error, archivo imagen {contador} no subido.</li>'

    else:  # se subio solo 1 archivo
        # print('no es lista')  # test
        resultado = revisar_foto(fotos)
        errores += resultado[0]
        if resultado[1] > 0:
            errores += f'<li>Error, ningún archivo de imagen subido.</li>'

# ===================== LUGAR =====================
sector = form['sector'].value
if len(sector) > 100:
    errores += f'<li>Por favor, ingrese un SECTOR de menos de 100 caracteres. ({len(sector)} caracteres usados).</li>'

# ===================== CONTACTO =====================
celular = form['celular'].value
regex2 = '^(\+?56)?(\s?)(0?9)(\s?)[9876543]\d{7}$'
if celular != '' and not (check(regex2, celular)):
    errores += '<li>Por favor, ingrese un número CELULAR de formato válido. (+56 9 1234 5678).</li>'

# ===================== ACTIVIDAD =====================
termino = form['dia-hora-termino'].value
regex3 = '^(\d\d\d\d)-(0?[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])\s(00|0[0-9]|1[0-9]|2[0-3]):(0[0-9]|[0-5][0-9])$'
if termino != '' and not (check(regex3, termino)):
    errores += '<li>Por favor, ingrese un HORARIO DE TERMINO de formato correcto.</li>'

# ======================== RRSS =====================
def validar_user(usuario):
    return 4 <= len(usuario) <= 50

### A continuación hay dos diccionarios con las tuplas para facilitar el llamado posterior

if not (type(fotos) == list):
    fotos = [fotos]

if tema == 'otro':
    # print(otro_tema)
    db.guardar_tema(Otro_tema)
    nuevo_temaID = db.get_temaID(Otro_tema)
    tema = nuevo_temaID[0][0]

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
            <script>window.location.href="home.py"</script>
"""

utf8stdout.write(listo)