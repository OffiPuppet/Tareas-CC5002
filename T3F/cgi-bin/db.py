# !/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import mysql.connector
import hashlib
import datetime
import numpy as np
import random
import os
sys.stdout.reconfigure(encoding='utf-8')


class DB:
    def __init__(self, host, user, password, database):
        self.db = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.db.cursor()

    # METODOS PARA CONSULTAR DB. 
    def get_tema_id(self, tema):
        sql = f'''
           SELECT id FROM tema WHERE id ={tema};
            '''
        self.cursor.execute(sql)
        return self.cursor.fetchall()[0][0]

    def get_data_listado(self, inicio):
        sql = f'''
            SELECT AC.id, CO.nombre, AC.sector, AC.nombre, AC.email, AC.celular, AC.dia_hora_inicio, AC.dia_hora_termino, AC.descripcion, TE.nombre 
            FROM actividad AC, comuna CO, tema TE 
            WHERE AC.comuna_id=CO.id AND AC.tema_id=TE.id 
            ORDER BY id DESC LIMIT {inicio}, 5;
        '''
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def get_data(self):
        sql = f'''
            SELECT AC.id, CO.nombre, AC.sector, AC.nombre, AC.email, AC.celular, AC.dia_hora_inicio, AC.dia_hora_termino, AC.descripcion, TE.nombre, F.ruta_archivo
            FROM actividad AC, comuna CO, tema TE, foto F
            WHERE F.actividad_id = AC.id AND AC.comuna_id=CO.id AND AC.tema_id=TE.id
            ORDER BY id DESC LIMIT 5;
            '''
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def get_actividad_list(self):
        sql = '''
        SELECT actividad.id, actividad.dia_hora_inicio, actividad.dia_hora_termino, comuna.nombre AS comuna,
        actividad.sector, tema.nombre, actividad.nombre, fotos.numero 
        FROM actividad, tema, comuna,
        (SELECT actividad_id, COUNT(actividad_id) AS numero 
        FROM foto GROUP BY actividad_id) AS fotos
        WHERE actividad.comuna_id = comuna.id AND actividad.id= fotos.actividad_id AND actividad.tema_id = tema.id;
        '''
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        return data

    def get_home_data(self):
        sql = f'''
        SELECT AC.id, AC.dia_hora_inicio, AC.dia_hora_termino, C.nombre, AC.sector, AC.tema_id, AC.descripcion, F.ruta_archivo
        FROM actividad AC, comuna C, (
            SELECT * FROM foto GROUP BY actividad_id
        ) F
        WHERE AC.id = F.actividad_id AND AC.comuna_id = C.id
        ORDER BY AC.id DESC
        LIMIT 5;
        '''
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def get_fotos(self, id_actividad):
        sql = f'''
        SELECT id, ruta_archivo, nombre_archivo, actividad_id FROM foto WHERE actividad_id={id_actividad};
        '''
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def contar_fotos(self, id_actividad):
        sql = f'''
            SELECT COUNT(id) FROM foto WHERE actividad_id={id_actividad};
        '''
        self.cursor.execute(sql)
        return self.cursor.fetchall()[0][0]

    def get_temas(self, id_tema):
        sql = f'''
            SELECT nombre FROM tema
            WHERE id = {id_tema};
            '''
        self.cursor.execute(sql)
        return self.cursor.fetchall()[0][0]

    def contar_actividades(self):
        sql = f'''
            SELECT COUNT(id) FROM `actividad`;
        '''
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def get_contactar_por(self, id_actividad):
        sql = f'''
            SELECT id, nombre, identificador, actividad_id FROM contactar_por WHERE actividad_id={id_actividad} ORDER BY nombre ASC;
        '''
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def get_month_hour(self):
        sql ='''
        SELECT DATE_FORMAT(dia_hora_inicio, "%Y-%m") AS año_mes,
        DATE_FORMAT(dia_hora_inicio,"%H:%i") AS hh_mm
        FROM actividad
        ORDER BY DATE_FORMAT(dia_hora_inicio, "%Y-%m");
        '''
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        return data

    def get_regiones(self):
        sql = '''
            SELECT id, nombre FROM `region` ORDER BY id ASC;
        '''
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def get_region_name(self, region_id):
        sql = f'''
        SELECT nombre FROM region WHERE id = '{region_id}'
        '''
        self.cursor.execute(sql)
        return self.cursor.fetchall()[0][0]

    def get_actividad_info(self, actividad_id):
        sql = f'''
        SELECT AC.id, CO.nombre, CO.id, AC.sector, AC.nombre, AC.email, AC.celular, AC.dia_hora_inicio, AC.dia_hora_termino, AC.descripcion, TE.nombre, COUNT(FO.id)
        FROM actividad AC, comuna CO, tema TE, foto FO
        WHERE AC.id = '{actividad_id}' AND FO.actividad_id = AC.id AND AC.comuna_id = CO.id AND AC.tema_id=TE.id;
        '''
        self.cursor.execute(sql)
        return self.cursor.fetchall()[0]

    def get_actividad_red(self, actividad_id):
        sql = f'''
        SELECT * FROM contactar_por WHERE actividad_id = '{actividad_id}'
        ORDER BY id ASC
        '''
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def get_comuna_data(self, comuna_id):
        sql = f'''
        SELECT nombre, region_id FROM comuna WHERE id = '{comuna_id}'
        '''
        self.cursor.execute(sql)
        return self.cursor.fetchall()[0]

    def get_comuna_id(self, nombre_comuna, region_id):
        sql = f'''
        SELECT id FROM comuna 
        WHERE nombre = '{nombre_comuna}' 
        AND region_id = {region_id};
        '''
        self.cursor.execute(sql)
        return self.cursor.fetchall()[0][0]

    def get_region_id(self, id_region):
        sql = f'''
        SELECT id FROM region
        WHERE id = '{id_region}';
        '''
        self.cursor.execute(sql)
        return self.cursor.fetchall()[0][0]

    def get_tema_id(self, tema):
        sql = f'''
           SELECT id FROM tema
           WHERE id ='{tema}';
            '''
        self.cursor.execute(sql)
        return self.cursor.fetchall()[0][0]

    def get_comunas(self, region_id):
        sql = f'''
            SELECT id, nombre FROM `comuna` WHERE region_id={region_id} ORDER BY id ASC;
        '''
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def get_comuna_data1(self, region_id):
        sql = f'''
            SELECT id, nombre FROM `comuna` WHERE region_id={region_id} ORDER BY id ASC;
        '''
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def get_comuna_data2(self, region_id):
        sql = f'''
            SELECT * FROM `comuna` WHERE region_id={region_id} ORDER BY region_id, nombre ASC;
        '''
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def get_comuna_data3(self):
        sql = '''
            SELECT id FROM `comuna`ORDER BY id ASC;
        '''
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def get_comuna_fotos(self):
        sql ='''
        SELECT comuna.nombre, COUNT(foto.id), comuna.id AS nfotos
        FROM actividad, comuna, foto
        WHERE actividad.comuna_id=comuna.id 
        AND foto.actividad_id = actividad.id
        GROUP BY comuna.nombre;
        '''
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        return data

    def get_nombre_tema(self,tema_id):  
        sql = f'''
            SELECT nombre FROM tema WHERE id={tema_id}
        '''
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def get_mapa_info(self, id):
        sql = f'''
        SELECT actividad.id, comuna.nombre, DATE_FORMAT(actividad.dia_hora_inicio,"%Y-%m-%d %H:%i") AS inicio,
        actividad.tema_id, actividad.sector, foto.ruta_archivo
        FROM actividad, foto, comuna
        WHERE actividad.id = foto.actividad_id
        AND comuna_id = comuna.id
        AND comuna_id = "{id}"
        ORDER BY actividad.id;
        '''
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        return data

    def get_actividad(self):
        sql = '''
        SELECT * FROM actividad ORDER BY id DESC
        '''
        self.cursor.execute(sql)
        return self.cursor.fetchall()
    
    def get_actividad_por_date(self):
        sql ='''
        SELECT fecha, COUNT(fecha) 
        FROM (SELECT CAST(dia_hora_inicio AS date) AS fecha FROM actividad AS F1) F1 
        GROUP BY fecha;
        '''
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        return data

    def get_actividad_por_tema(self):
         sql ='''
          SELECT COUNT(T.nombre), T.nombre
          FROM tema T, actividad AC
          WHERE T.id = 2 and T.id = AC.tema_id
          GROUP BY T.nombre
          '''
         self.cursor.execute(sql)
         data = self.cursor.fetchall()
         return data
    
    def guardar_actividad1(self):

        sql = '''
                SELECT * FROM actividad
                '''
        id_actividad = self.cursor.getlastrowid()
        return id_actividad

    # METODOS PARA GUARDAR DB.
    def guardar_contacto(self, contacto):
        sql = '''
                INSERT INTO contactar_por (nombre, identificador, actividad_id)
                VALUES (%s, %s, %s)
             '''
        valores = (contacto['nombre'],
                   contacto['id'],
                   contacto['id_act'])
        self.cursor.execute(sql, valores)

    def guardar_actividad(self, actividad):

        sql = '''
                INSERT INTO actividad (comuna_id, sector, nombre, email, celular, dia_hora_inicio, dia_hora_termino, descripcion, tema_id)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                '''
        valores = (actividad['comuna'],
                   actividad['sector'],
                   actividad['nombre'],
                   actividad['email'],
                   actividad['celular'],
                   actividad['dia-hora-inicio'],
                   actividad['dia-hora-termino'],
                   actividad['descripcion'],
                   actividad['tema'])
        self.cursor.execute(sql, valores)  # ejecuta la consulta
        id_actividad = self.cursor.getlastrowid()
        return id_actividad

    def save_data(self, data):
        ##Se separa la data en 3 partes
        fotos = data[2]
        try:
            id_actividad = self.guardar_actividad1()  # guarda la actividad y recupera el id
            for foto in fotos:
                # Procesar archivo
                fileobj = foto
                filename = fileobj.filename

                # Cuenta los archivos que hay en la base de datos
                sql = "SELECT COUNT(id) FROM foto;"
                self.cursor.execute(sql)
                total = self.cursor.fetchall()[0][0] + 1

                filename_hash = hashlib.sha256(filename.encode()).hexdigest()[0:30]  # aplica función de hash
                # concatena la función de hash con el número total de archivos, nombre único
                filename_hash += f"_{total}"
                # OJO: lo anterior puede ser peligroso en el caso en que se tenga un servidor que ejecute peticiones en
                # paralelo. Lo que se conoce como un datarace. Nuestro servidor ejecuta sus procesos de forma secuencial,
                # no worries.

                # guarda el archivo localmente
                open(f"media/{filename_hash}", "wb").write(fileobj.file.read())
                sql_file = '''
                            INSERT INTO foto (ruta_archivo, nombre_archivo, actividad_id) 
                            VALUES (%s, %s, %s)
                            '''
                self.cursor.execute(sql_file, (filename_hash, filename, id_actividad))  # ejecuta la query que guarda el archivo en base de datos
            self.db.commit()  # modifico la base de datos

        except:
            print("ERROR AL GUARDAR EN LA BASE DE DATOS")
            sys.exit()

    def get_actividad_photos(self, actividad_id):
        sql = f'''
        SELECT * FROM foto WHERE actividad_id = '{actividad_id}'
        ORDER BY id ASC
        '''
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def get_last_actividad_id(self):
        sql = '''
        SELECT max(id) FROM actividad
        '''
        self.cursor.execute(sql)
        return self.cursor.fetchall()[0][0]

    def get_actividades(self):
        sql = '''
        SELECT * FROM actividad ORDER BY id DESC
        '''
        self.cursor.execute(sql)
        return self.cursor.fetchall()
    
    def get_all_actividades(self):
        sql = '''
            SELECT id, comuna_id, sector, nombre, email, celular, dia_hora_inicio, dia_hora_termino, descripcion, tema_id FROM actividad
            '''
        self.cursor.execute(sql)  # ejecuta la consulta
        return  self.cursor.fetchall() 

    # def get_tema_actividad(self):
    #     sql=f'''
    #     SELECT T.nombre, AC.id, COUNT(nombre) FROM tema T, actividad AC
    #     WHERE T.id = AC.id
    #     '''
    #     self.cursor.execute(sql)
    #     return self.cursor.fetchall()

    def get_actividad_list_data(self):
        sql = """
            SELECT AC.id, AC.dia_hora_inicio, AC.dia_hora_termino, C.nombre, AC.sector, AC.tema_id, AC.descripcion, AC.nombre, F1.ruta_archivo, F2.total_fotos
            FROM actividad AC, comuna C, ( SELECT * FROM foto GROUP BY actividad_id ) F1, (SELECT actividad_id, COUNT(*) AS total_fotos FROM foto GROUP BY actividad_id) F2
            WHERE AC.id = F1.actividad_id AND AC.id = F2.actividad_id AND AC.comuna_id = C.id AND AC.id > {5*page} AND E.id <= {5*(page+1)}
            ORDER BY AC.id ASC;
        """
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def count_actividades(self, id_actividad):
        sql = f"""
            SELECT COUNT(id) FROM actividad WHERE actividad_id='{id_actividad}';
        """
        self.cursor.execute(sql)
        return self.cursor.fetchall()[0][0]

    def get_min_comunas(self):
        sql = '''
        SELECT * FROM comuna GROUP BY region_id COUNT;
        '''
        self.cursor.execute(sql)
        return self.cursor.fetchall()
    
    def get_last_5(self):
        sql = f'''
            SELECT AC.id, CO.nombre, AC.sector, AC.nombre, AC.email, AC.celular, AC.dia_hora_inicio, AC.dia_hora_termino, AC.descripcion, TE.nombre
            FROM actividad AC, comuna CO, tema TE
            WHERE AC.comuna_id=CO.id AND AC.tema_id=TE.id
            ORDER BY id DESC LIMIT 5;
            '''
        self.cursor.execute(sql)
        return self.cursor.fetchall()
    
    def getMapa(self):
        self.cursor.execute('SELECT *, COUNT(*) FROM actividad GROUP BY comuna_id')
        return self.cursor.fetchall()

    #################################################
    ################QUERYS GRAFICOS##################
    #################################################

    def get_grafico1(self):
        format_date = lambda d: f"{d.year}-{d.month}-{d.day}"
        dates = sorted([v[6] for v in self.get_actividad()])
        
        data = list(map(format_date, [v for v in dates]))
        
        x = []
        y = []

        for v in data:
            if v not in x:
                x.append(v)
                y.append(1)
            else:
                y[x.index(v)] += 1

        return [[u, v] for u,v in zip(x, y)]

    def get_grafico2(self):
        data = [v[9] for v in self.get_actividad()]
        
        x = []
        y = []

        for v in data:
            if v not in x:
                x.append(v)
                y.append(1)
            else:
                y[x.index(v)] += 1

        return [{"label": u + int(f": {v}"), "data": v} for u,v in zip(x, y)]

    def get_grafico3(self):
        month_list = [
            ["Jan."],
            ["Feb."],
            ["Mar."],
            ["Apr."],
            ["May."],
            ["Jun."],
            ["Jul."],
            ["Aug."],
            ["Sep."],
            ["Oct."],
            ["Nov."],
            ["Dec."]
        ]
        
        
        frec = [
            list(np.zeros(12)),
            list(np.zeros(12)),
            list(np.zeros(12)) 
        ]

        data = [v[6] for v in self.get_actividad()]

        for d in data:
            month_index = d.month - 1
            time_period = None
            
            if d.hour < 11 and d.hour >= 0:
                time_period = 0
            elif d.hour >= 11 and d.hour < 15:
                time_period = 1
            else:
                time_period = 2
            
            frec[time_period][month_index] += 1

        ret_1 = [[month_list[i], frec[0][i]] for i in range(0, 12)]
        ret_2 = [[month_list[i], frec[1][i]] for i in range(0, 12)]
        ret_3 = [[month_list[i], frec[2][i]] for i in range(0, 12)]
        
        return ret_1, ret_2, ret_3

    def getMapActividad(self):
        self.cursor.execute('SELECT *, COUNT(*) FROM actividad GROUP BY comuna_id')
        return self.cursor.fetchall()
    
    def get_comuna(self, comuna_id):
        self.cursor.execute(f'SELECT nombre FROM comuna WHERE id = {comuna_id}')
        return self.cursor.fetchall()
    
    def get_photo(self, id):
        self.cursor.execute(f'SELECT ruta_archivo FROM foto WHERE actividad_id = {id}')
        return self.cursor.fetchall()