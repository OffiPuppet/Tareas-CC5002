# !/usr/bin/python3
# -*- coding: utf-8 -*-

import cgitb
from db import DB

cgitb.enable()
utf8stdout = open(1, 'w', encoding='utf-8', closefd=False)
db = DB("localhost", "root", "", "tarea2")
data = db.get_last_5()
msg = f'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.1/css/all.min.css" integrity="sha512-KfkfwYDsLkIlwQp6LFnl8zNdLGxu9YAA1QvwINks4PhcElQSvqcyVLLD9aMhXd13uQjoXtEKNosOWaZqXgel0g==" crossorigin="anonymous" referrerpolicy="no-referrer" />
    <link rel="stylesheet" href="../principal.css">
    <title>CSCE</title>
    <link rel="stylesheet" href="https://unpkg.com/leaflet@1.8.0/dist/leaflet.css" integrity="sha512-hoalWLoI8r4UszCkZ5kL8vayOGVae1oxXe/2A4AO6J9+580uKHDO3JdHb7NzwwzK5xr/Fs0W40kiNHxM9vyTtQ==" crossorigin="" />
    <script src="https://unpkg.com/leaflet@1.8.0/dist/leaflet.js" integrity="sha512-BB3hKbKWOc9Ez/TAwyWxNXeoV9c1v6FIeYiBieIWkpLjauysF18NzgR1MBNBXf8/KABdlkX68nAhlwcDFLGPCQ==" crossorigin=""></script>
    <script type="module" src="https://unpkg.com/ionicons@5.5.2/dist/ionicons/ionicons.esm.js"></script>
    <script nomodule src="https://unpkg.com/ionicons@5.5.2/dist/ionicons/ionicons.js"></script>
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
                    <a href="form.py">
                        <span class="icon"><ion-icon name="accessibility-outline"></ion-icon></span>
                        <span class="title">Agregar Actividad</span>
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
            </ul>
        </div>

        <div class="main">
            <div class="toggle1"></div>
                <div class="topbar">
                    <div class="toggle">
                        <ion-icon name="menu-outline"></ion-icon>
                    </div>
                </div>
            <div class="bienvenida"></div>
                <div class="table">
                    <div class="recentActivity">
                        <div class="header">
                            <h1>Le damos la bienvenida a CSCE</h1>
'''

if len(data) == 0:
    msg += '''
            <p>¡Ups! Parece que todavia no hay actividades registadas</p>
            </div>'''
            
else:
    msg += '''
            <p>Aquí tienes las últimas 5 actividades registradas</p>           
            </div>
            <br>
            <br>
            <br>
            <br>
            <div class="table">
                <table>
                    <thead>
                        <tr>
                            <td>Inicio</td>
                            <td>Término</td>
                            <td>Comuna</td>
                            <td>Sector</td>
                            <td>Tema</td>
                        </tr>
                    </thead>
                    <tbody>
    '''
    for t in data:
        (id, nombre_comuna, sector, nombre, email, celular, d_h_i, d_h_t, descripcion, tema_nombre) = t
        msg += f'''
                            <tr>
                                <td>{d_h_i}</td>
                                <td>{d_h_t}</td>
                                <td>{nombre_comuna}</td>
                                <td>{sector}</td>
                                <td>{tema_nombre}</td>
                            </tr>
                        '''
    msg += '''    
                        </tbody>
                    </table>
                </div>
            '''

msg += '''
            <br>
        </div>
    </div>
    <div id="map" style="height: 640px;"></div>
    <div class="footer"></div>

</body>

<script>
    var mymap = L.map('map').setView([-33.4500000, -70.6666667], 4);
    L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    id: 'mapbox/streets-v11',
    tileSize: 512,
    zoomOffset: -1,
    accessToken: 'your.mapbox.access.token'
    }).addTo(mymap);
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
                let rsp = xmlhttp.responseText;
                let ubications = JSON.parse(rsp);
                for (let i=0; i<ubications.length; i++){
                    let marker = L.marker(ubications[i][1], {title: "N° Fotos ="+ubications[i][2]}).addTo(mymap);
                    marker.bindPopup(String(ubications[i][0]), {maxHeight:250, minWidth:570,maxWidth:660});
                    marker.on('click', onClick);
                    function onClick(e) {
                        var popup = e.target.getPopup();
                        let id = popup.getContent();
                        popup.setContent('Espere...')
                        var xmlhttp2 = new XMLHttpRequest();
                        xmlhttp2.onreadystatechange = function () {
                            if (this.readyState == 4 && this.status == 200) {
                                    let inner  = xmlhttp2.responseText;
                                    popup.setContent(inner);
                                    e.target.off('click', onClick);
                            }
                        }
                        xmlhttp2.open("GET", "mapa_info.py?id="+id, true);
                        xmlhttp2.send();
                    }
                }
            }
        }
    xmlhttp.open("GET", "mapa.py", true);
    xmlhttp.send();
</script>

<script>
    //Menu toggle
    let toggle = document.querySelector('.toggle');
    let navigation = document.querySelector('.navigation');
    let main = document.querySelector('.main');

    toggle.onclick = function(){
        navigation.classList.toggle('active');
        main.classList.toggle('active');
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
    const toggle1 = document.querySelector('.toggle1');
    toggle1.onclick = function(){
        sec.classList.toggle('dark')
        sec1.classList.toggle('dark')
    }
</script>
</html>
'''

utf8stdout.write(msg)