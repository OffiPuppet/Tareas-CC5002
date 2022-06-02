import cgi
import math
from db import DB

utf8stdout = open(1, 'w', encoding='utf-8', closefd=False)
db = DB("localhost","root", "", "tarea2")
data = db.get_data()
id0 = cgi.FieldStorage().getfirst("id")
all_act = db.get_actividad_list()

if id0 is None:
    id0 = 0
my_id = int(id0)

ultima_pagina = len(data) // 5 if len(data) % 5 != 0 else (len(data) // 5) - 1

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
    <script type="module" src="https://unpkg.com/ionicons@5.5.2/dist/ionicons/ionicons.esm.js"></script>
    <script nomodule src="https://unpkg.com/ionicons@5.5.2/dist/ionicons/ionicons.js"></script>
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
                <div class="topbar">
                    <div class="toggle">
                        <ion-icon name="menu-outline"></ion-icon>
                    </div>
                </div>
            <div class="bienvenida">
            </div>
            <div class="table">
                <div class="recentActivity">
                    <div class="header">
                        <h2>Lista de Actividades Agregadas</h2>
'''

if len(data) == 0:
    msg += '''
            <p>¡Ups! Parece que todavia no hay actividades registadas</p>
            </div>
            <div class="topbar">
                <div class="toggle">
                    <ion-icon name="menu-outline"></ion-icon>
                </div>
            </div>'''
            
else:
    msg += '''        
            </div>
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
                            <td>N° Fotos</td>
                        </tr>
                    </thead>
                    <tbody>
    '''
    for t in all_act:
        (id, d_h_i, d_h_t, nombre_comuna, sector, tema_nombre, nombre_org, foto) = t
        msg += f'''         
                            <tr class="clickable-row" onclick="window.location.href = './info_actividad.py?actividad_id={id}'">
                                <td>{d_h_i}</td>
                                <td>{d_h_t}</td>
                                <td>{nombre_comuna}</td>
                                <td>{sector}</td>
                                <td>{tema_nombre}</td>
                                <td>{foto}</td>
                            </tr>
                        '''
    msg += '''    
                        </tbody>
                    </table>
                </div>
            '''

msg += f'''
            <br>
    <div class="footer"></div>
    <div class="volver">
        <ul>
            <li>
                <a href="list.py?id=0">Primera página</a>&nbsp;&nbsp;
            </li>
        </ul>
        <ul>
            <li>
                <a href="list.py?id={my_id - 1}">Página Anterior</a> &nbsp;&nbsp;
            </li>
        </ul>
        <ul>
            <li>
                <a href="list.py?id={my_id + 1}">Siguiente página</a>&nbsp;&nbsp;
            </li>
        </ul>
        <ul>
            <li>
               <a href="list.py?id={ultima_pagina}">Última página</a>
            </li>
        </ul>
    </div>
    </div>
</body>'''

msg += '''
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
</html>
'''

utf8stdout.write(msg)