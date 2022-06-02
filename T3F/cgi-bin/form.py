# !/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from db import DB

print("Content-type: text/html; charset=UTF-8")
print()
sys.stdout.reconfigure(encoding='utf-8')

db = DB("localhost", "root", "", "tarea2")
utf8stdout = open(1, "w", encoding="utf-8", closefd=False)

html = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AgregarActividad</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.1/css/all.min.css" integrity="sha512-KfkfwYDsLkIlwQp6LFnl8zNdLGxu9YAA1QvwINks4PhcElQSvqcyVLLD9aMhXd13uQjoXtEKNosOWaZqXgel0g==" crossorigin="anonymous" referrerpolicy="no-referrer" />
    <link rel="stylesheet" href="../style.css">
    <script src="../T1.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/sweetalert2@11.4.8/dist/sweetalert2.all.min.js"></script>

</head>


<body>
  <div class="container">
    <div class="navigation">
        <ul>
            <li>
                <a href="">
                    <span class="title">CSCE</span>
                </a>
            </li>
            <li>
              <a href="list.py?id=0">
                    <span class="icon"><ion-icon name="book-outline"></ion-icon></span>
                    <span class="title">Ver listado de actividades</span>
                </a>
            </li>
            <li>
                <a href="estadisticas.py">
                    <span class="icon"><ion-icon name="stats-chart-outline"></ion-icon></span>
                    <span class="title">Estadísticas</span>
                </a>
            </li>
            <li>
              <a href="home.py">
                  <span class="icon"><ion-icon name="home-outline"></ion-icon></span>
                  <span class="title">Volver al inicio</span>
              </a>
          </li>
        </ul>
    </div>

    <div class="main">
      <div class="toggle1"></div>
        <div class="topbar">
            <div class="toggle">
                <ion-icon name="menu-outline"></ion-icon>
            </div>
        </div>
    </div>

    <div class="form">
        <form id="form" name="form" method="POST" action="save_data.py" enctype="multipart/form-data">
            <label>Información del Lugar:</label><br>
            <div class="nombre"><br>
                <label id="region">Región</label>
                <select id="region1" class="form-control" name="region" onchange="cambiaComuna()">
                    <option value="0" selected>Escoga su Región</option>
                    <option value="1">Región de Tarapacá</option> 
                    <option value="2">Región de Antofagasta</option>
                    <option value="3">Región de Atacama</option>
                    <option value="4">Región de Coquimbo </option>
                    <option value="5">Región de Valparaíso</option>
                    <option value="6">Región del Libertador Bernardo Ohiggins</option>
                    <option value="7">Región del Maule</option>
                    <option value="8">Región del Biobío</option>
                    <option value="9">Región de La Araucanía</option>
                    <option value="10">Región de Los Lagos</option>
                    <option value="11">Región Aisén del General Carlos Ibáñez del Campo</option>
                    <option value="12">Región de Magallanes y la Antártica Chilena</option>
                    <option value="13">Región Metropolitana de Santiago </option>
                    <option value="14">Región de Los Ríos</option>
                    <option value="15">Región Arica y Parinacota</option>
                    <option value="16">Región del Ñuble</option>
                    </select>
                    <label id="comuna">Comuna</label>
                    <select id="comuna1" name="comuna">
                      <option value="-">-</option>
                      </select>
                    <br>
                    <br>
                    <label for="sector">Sector</label>
                      <input size="100" maxlength="100" type="text" class="sector" name="sector" id="sector" placeholder="Sector"><br>
            </div>
            <br>
            <br>
            <label>Información de la persona que organiza:</label>
            <div class="nombre">
              <br>
              <label for="nombre">Nombre</label>
              <input size="100" maxlength="200" type="text" class="form-control" name="nombre" id="nombre" placeholder="Nombre">
            </div>
            <div class="email">
              <br>
              <label for="email">Email</label>
              <input size="100" type="text" class="form-control" name="email" id="email" placeholder="Email">
            </div>
            <div class="celular">
              <br>
              <label for="celular">Celular</label>
              <input size="15" type="text" class="form-control" name="celular" id="celular" placeholder="Celular">
            </div>

            <div class="contactar" id="contactar-g">
              <br>
              <label for="contactar">Contactar por</label>
              <select id="contactar" class="form-control" name="contactar-por" onchange="cambiaContacto()">
                <option value="Ninguna" selected>Escoga contacto</option>
                <option value="Facebook">Facebook</option> 
                <option value="Instagram">Instagram</option>
                <option value="Telegram">Telegram</option>
                <option value="TikTok">TikTok</option>
                <option value="Twitter">Twitter</option>
                <option value="WhatsApp">WhatsApp</option>
                <option value="Otra">Otra</option>
              </select>
              <input id="inputcontacto" name="inputcontacto" type="text">
              <button type="button" onclick="AddContacto()">Agregar Contacto</button>
            </div>
            <div id="clones"></div>
            <br> 
            <br>
            <label>Información de la actividad:</label>
            <br>
            <div class="dia-hora-inicio">
              <br>
              <label for="dia-hora-inicio">Dia Hora Inicio</label>
              <input type="text" size="20" maxlength="200" class="form-control" name="dia-hora-inicio" id="dia-hora-inicio" onchange="refillDate()">
            </div>
            <br>
            <div class="dia-hora-termino">
              <br>
              <label for="dia-hora-termino">Dia Hora Término</label>
              <input size="20" maxlength="200" type="text" class="form-control" name="dia-hora-termino" id="dia-hora-termino" placeholder="AAAA-MM-DD HH:MM">
            </div>
            <br>
            <div class="descripcion-evento">
              <label for="descripcion-evento">Descripción</label>
              <br>
              <textarea class="form-control" id="descripcion-evento" name="descripcion-evento" maxlength="1000" rows="10" cols="50" placeholder="Máximo 1000 caracteres"></textarea>
            </div>
            <br>
            <div class="tema">
                <br>
                <label>Tema</label>
                <select id="tema" name="tema" onchange="cambiaTema()">
                  <option value="0" selected>Escoga contacto</option>
                  <option value="1">música</option>
                  <option value="2">deporte</option>
                  <option value="3">ciencias</option>
                  <option value="4">religión</option>
                  <option value="5">política</option>
                  <option value="6">tecnología</option>
                  <option value="7">juegos</option>
                  <option value="8">baile</option>
                  <option value="9">comida</option>
                  <option value="10">Otro</option>
                </select>
            </div>
            <div class="inputTema">
              <input id="inputTema" type="text" name="inputTema" placeholder="Tema" disabled>
            </div>
            <br>
            <div class="form-control">
              <br>
              <label>Subir Foto</label>
              <input type="file" id="foto-actividad" name="foto-actividad">
              <button type="button" onclick="AddPhoto()">Agregar Foto</button>
              <div id="contenedorObjetos"></div>
            </div>
            <br>
            <button type="submit" class="form-control">Agregar esta Actividad</button>
            <div class="b_container" id="confirmation"></div>
        </form>
    </div>

    <div class="error"></div>
        <div class="errores">
        <div id="contenedorErrores" class="contenedor"></div>
    </div>
  </div>

<script type="module" src="https://unpkg.com/ionicons@5.5.2/dist/ionicons/ionicons.esm.js"></script>
<script nomodule src="https://unpkg.com/ionicons@5.5.2/dist/ionicons/ionicons.js"></script>
<script>
    //Menu toggle
    let toggle = document.querySelector('.toggle');
    let navigation = document.querySelector('.navigation');
    let main = document.querySelector('.main');
    let form = document.querySelector('.form');

    toggle.onclick = function(){
        navigation.classList.toggle('active');
        main.classList.toggle('active');
        form.classList.toggle('active');
    }
    //Add hovered class
    let list = document.querySelectorAll('.navigation li');
    function activeLink(){
        list.forEach((item) =>
        item.classList.remove('hovered'));
        this.classList.add('hovered');
     }
     list.forEach((item) =>
     item.addEventListener('mouseover', activeLink));
</script>
<script>
    const sec = document.querySelector('.main');
    const sec1 = document.querySelector('.navigation');
    const form1 = document.querySelector('.form');
    const icon = document.querySelector('.toggle');
    const toggle1 = document.querySelector('.toggle1');
    toggle1.onclick = function(){
        sec.classList.toggle('dark')
        sec1.classList.toggle('dark')
        form1.classList.toggle('dark')
        icon.classList.toggle('dark')
    }
</script>
</body>
</html>'''

print(utf8stdout.write(html))