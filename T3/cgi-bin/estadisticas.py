# !/usr/bin/python3
# -*- coding: utf-8 -*-

import cgi
import cgitb
import json
from db import DB

cgitb.enable()
utf8stdout = open(1, 'w', encoding='utf-8', closefd=False)
db = DB("localhost","root", "", "tarea2")

msg = f'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.1/css/all.min.css" integrity="sha512-KfkfwYDsLkIlwQp6LFnl8zNdLGxu9YAA1QvwINks4PhcElQSvqcyVLLD9aMhXd13uQjoXtEKNosOWaZqXgel0g==" crossorigin="anonymous" referrerpolicy="no-referrer" />
    <link rel="stylesheet" href="../CSS/principal.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <title>CSCE</title>
    <script src='../code/highcharts.js'></script>
    <script src="../code/modules/exporting.js"></script>
    <script src="../code/modules/export-data.js"></script>
    <script src="../code/modules/accessibility.js"></script>
    <script src='../JS/graficos.js'></script>
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
                <div id="lineplot"></div>
                <div id="pieplot"></div>
                <div id="barplot"></div>'''

msg += '''
            <br>
        </div>
        </div>
    <div class="footer"></div>
</body>

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
<script>
        function requestLine(){
            var xmlhttp = new XMLHttpRequest();
            xmlhttp.onreadystatechange = function () {
                if (this.readyState == 4 && this.status == 200) {
                    let line = xmlhttp.responseText;
                    let line1 = JSON.parse(line);
                    let line2 = Object.keys(line1);
                    let line_div = document.getElementById('lineplot');
                    let line_layout = create_layout('N° de actividades por día', 'Fecha', 'Número de actividades', line1[line2[0]]);
                    Highcharts.chart(line_div, line_layout);
                }
            }
            xmlhttp.open("GET", "glinea.py", true);
            xmlhttp.send();
        }

        function requestPie(){
            var xmlhttp = new XMLHttpRequest();
            xmlhttp.onreadystatechange = function () {
                if (this.readyState == 4 && this.status == 200) {
                    let pie = xmlhttp.responseText;
                    let pie_div = document.getElementById('pieplot');
                    let pie_layout = create_layout1('N° de actividades por tema', 'Fecha', 'Número de actividades', JSON.parse(pie));
                    Highcharts.chart(pie_div, pie_layout);
                }
            }
            xmlhttp.open("GET", "gtorta.py", true);
            xmlhttp.send();
        }
        
        function requestBar(){
            var xmlhttp = new XMLHttpRequest();
            xmlhttp.onreadystatechange = function () {
                if (this.readyState == 4 && this.status == 200) {
                    let bar = xmlhttp.responseText;
                    let bar_div = document.getElementById('barplot');
                    let bar_layout = create_layout2('N° de actividades según mes y hora del día', 'Mes', 'Cantidad', JSON.parse(bar));
                    Highcharts.chart(bar_div, bar_layout);
                }
            }
            xmlhttp.open("GET", "gbarra.py", true);
            xmlhttp.send();
        }

        requestLine();
        requestPie();
        requestBar();
    </script>
</html>
'''

utf8stdout.write(msg)