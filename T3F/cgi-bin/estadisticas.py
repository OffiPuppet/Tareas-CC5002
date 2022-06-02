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
    <link rel="stylesheet" href="../principal.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <title>CSCE</title>
    <script src='../graficos1.js'></script>
    <script src='https://code.highcharts.com/modules/oldie-polyfills.js'></script>
    <script src='../code/highcharts.js'></script>
    <script src='../code/modules/exporting.js'></script>
    <script src='../code/modules/export-data.js'></script>
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
                        <span class="icon"><ion-icon name="stats-chart-outline"></ion-icon></span>
                        <span class="title">Volver al inicio</span>
                    </a>
                </li>
            </ul>
        </div>

        <div class="main">
            <div class="toggle1"></div>
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
    const sec = document.querySelector('.main');
    const sec1 = document.querySelector('.navigation');
    const toggle1 = document.querySelector('.toggle1');
    toggle1.onclick = function(){
        sec.classList.toggle('dark')
        sec1.classList.toggle('dark')
}
</script>
<script>
    requestLine()
</script>
</html>
'''

utf8stdout.write(msg)