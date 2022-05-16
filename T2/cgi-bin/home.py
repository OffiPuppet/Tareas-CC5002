import cgitb
from db import DB

cgitb.enable()
utf8stdout = open(1, 'w', encoding='utf-8', closefd=False)
db = DB("localhost","root", "", "tarea2")
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
    <script src="../T2.js"></script>
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
                            <td>Foto</td>
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
                                <td><img class="table-image" src=src="../media/{descripcion}"></td>
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
</html>
'''

utf8stdout.write(msg)