#!/usr/bin/python3
# -*- coding: utf-8 -*-

import cgi
import cgitb
from db import DB

cgitb.enable()
utf8stdout = open(1, 'w', encoding='utf-8', closefd=False)
actividad_id = int(cgi.FieldStorage()["actividad_id"].value)
db = DB("localhost","root", "", "tarea2")

# Recuperamos informacion de la base de datos:
(actividad_id, comuna_nombre, comuna_id, sector, nombre, email, celular, d_h_i, d_h_t, desc, nombre_tema, count) = db.get_actividad_info(actividad_id)
datos_comuna = db.get_comuna_data(comuna_id)
print(datos_comuna)
comuna = datos_comuna[0]
region = db.get_region_name(datos_comuna[1])
rrss_actividad = db.get_actividad_red(actividad_id)
fotos_actividad = db.get_actividad_photos(actividad_id)


html = f'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.1/css/all.min.css" integrity="sha512-KfkfwYDsLkIlwQp6LFnl8zNdLGxu9YAA1QvwINks4PhcElQSvqcyVLLD9aMhXd13uQjoXtEKNosOWaZqXgel0g==" crossorigin="anonymous" referrerpolicy="no-referrer" />
    <link rel="stylesheet" href="../CSS/principal.css">
    <script src="../JS/T1.js"></script>
    <title>CSCE</title>
    <script src="https://cdn.jsdelivr.net/npm/sweetalert2@11.4.8/dist/sweetalert2.all.min.js"></script>
    
</head>
<body>
    <div class="container">
        <div class="navigation">
                <ul>
                    <li>
                        <a href="home.py">
                            <span class="title">CSCE</span>
                        </a>
                    </li>
                    <li>
                        <a href="form.py">
                            <span class="icon"><ion-icon name="accessibility-outline"></ion-icon></span>
                            <span class="title">Agregar Actividad</span>
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
                <div class="bienvenida"></div>
                <div class="table">
                    <div class="recentActivity">
                        <div class="header">
                            <h2>Informacion Detallada</h2>         
                </div>
            <div id="event-info">
            <br>
                <div class="info1">
                    <h1>Información del lugar</h1>
                </div>
                <hr class="section-separator">
                <br>
                <div class="section-info">
                    <div class="section-info-line">
                        <div class="info-left">
                            <p>Región:<p>
                        </div>
                        <div class="info-right">
                            <p>{region}</p>
                        </div>
                    </div>
                    <br>
                    <div class="section-info-line">
                        <div class="info-left">
                            <p>Comuna:</p>
                        </div>
                        <div class="info-right">
                            <p>{comuna}</p>
                        </div>
                    </div>
                    <br>
                    <div class="section-info-line">
                        <div class="info-left">
                            <p>Sector:<p>
                        </div>
                        <div class="info-right">
                            <p>{sector}</p>
                        </div>
                    </div>
                </div>
                <br>
                <div class="info1">
                    <h1>Datos Organizador(a)</h1>
                </div>
                <hr class="section-separator">
                <br>
                <div class="section-info">
                    <div class="section-info-line">
                        <div class="info-left">
                            <p>Nombre:</p>
                        </div>
                        <div class="info-right">
                            <p>{nombre}</p>
                        </div>
                    </div>
                    <br>
                    <div class="section-info-line">
                        <div class="info-left">
                            <p>Email:</p>
                        </div>
                        <div class="info-right">
                            <p>{email}</p>
                        </div>
                    </div>
                    <br>
                    <div class="section-info-line">
                        <div class="info-left">
                            <p>Número de Celular:</p>
                        </div>
                        <div class="info-right">
                            <p>{celular}</p>
                        </div>
                    </div>
                </div>
'''
# Mostrar apartado redes sociales si estan registradas.
if len(rrss_actividad)>0:
    html += ''' 
                <div class="info1">
                    <h1>Redes sociales del (de la) Organizador(a)</h1>
                </div>
                <hr class="section-separator">
                <div class="section-info">
    '''
    for rs in rrss_actividad:
        html += f'''
                    <br>
                    <div class="section-info-line">
                        <div class="info-left">
                            <p>{rs[1]}</p>
                        </div>
                        <div class="info-right">
                            <p>{rs[2]}</p>
                        </div>
                    </div>
        '''
    
    html += '''</div>'''


html += f'''    
                <br>
                <div class="info1">
                    <h1>Información del Evento</h1>
                </div>
                <hr class="section-separator">
                <br>
                <div class="section-info">
                    <div class="section-info-line">
                        <div class="info-left">
                            <p>Día y hora de inicio:</p>
                        </div>
                        <div class="info-right">
                            <p>{d_h_i}</p>
                        </div>
                    </div>
                    <br>
                    <div class="section-info-line">
                        <div class="info-left">
                            <p>Día y hora de término:</p>
                        </div>
                        <div class="info-right">
                            <p>{d_h_t}</p>
                        </div>
                    </div>
                    <br>
                    <div class="section-info-line">
                        <div class="info-left">
                            <p>Descripción:</p>
                        </div>
                        <div class="info-right">
                            <p>{desc}</p>
                        </div>
                    </div>
                    <br>
                    <div class="section-info-line">
                        <div class="info-left">
                            <p>Tema:</p>
                        </div>
                        <div class="info-right">
                            <p>{nombre_tema}</p>
                        </div>
                    </div>
                    <br>
'''

# Mostrar foto principal:
html += f'''
                    <div class="section-info-line">
                        <div class="info-left">
                            <p>Foto principal:<p>
                        </div>
                        <br>
                        <div class="info-right">
                            <img src="../media/{fotos_actividad[0][1]}" width="320" height="240" onclick='agrandar(src)>
                        </div>
                    </div>
'''
# En caso de existir mas fotos, tambien se muestran:
resto_fotos = fotos_actividad[1:]

if len(resto_fotos) > 0:
    k = 1
    for f in resto_fotos:
        html += f'''
                    <div class="section-info-line">
                        <div class="info-left">
                            <p>Fotos extras: {k}<p>
                        </div>
                        <div class="info-right">
                            <img class="event-image" src="../media/{f[1]}" width="320" height="240" onclick='agrandar(src)'>
                        </div>
                    </div>
                    <div class="volver">
                    <ul>
                        <li>
                            <a class="event-list-btn" id="home-btn" href="./list.py?page=0">Volver a la lista de actividades</a>
                        </li>
                    </ul>
                    <br>
                    <ul>
                        <li>
                            <a class="event-list-btn" id="return-btn" href="./home.py">Volver al inicio</a>
                        </li>
                    </ul>
                </div>
        
        '''
else:
    html += '''          
                    </div>
                </div>
                <br>
                <div class="volver">
                    <ul>
                        <li>
                            <a class="event-list-btn" id="home-btn" href="./list.py?page=0">Volver a la lista de actividades</a>
                        </li>
                    </ul>
                    <br>
                    <ul>
                        <li>
                            <a class="event-list-btn" id="return-btn" href="./home.py">Volver al inicio</a>
                        </li>
                    </ul>
                </div>
            </div>
            <!-- IMG VIEW: CONTENIDO DEL POP-UP ASOCIADO A LA VISTA DE UNA IMAGEN -->
            <div class="image-view" id="image-view">
                <div id="image-view-body" class="image-view-body"></div>
            </div>
            <div id="image-view-overlay"></div>
        </div>
    </body>

<script>
    const sec = document.querySelector('.main');
    const sec1 = document.querySelector('.navigation');
    const toggle1 = document.querySelector('.toggle1');
    toggle1.onclick = function(){
        sec.classList.toggle('dark')
        sec1.classList.toggle('dark')
    }
</script>

</html>
''' 

utf8stdout.write(html)