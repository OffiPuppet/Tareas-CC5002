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
            SELECT AC.id, CO.nombre, AC.sector, AC.nombre, AC.email, AC.celular, AC.dia_hora_inicio, AC.dia_hora_termino, AC.descripcion, TE.nombre FROM actividad AC, comuna CO, tema TE WHERE AC.comuna_id=CO.id AND AC.tema_id=TE.id ORDER BY id DESC LIMIT {inicio}, 5;
        '''
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def get_data(self):
        sql = f'''
            SELECT AC.id, CO.nombre, AC.sector, AC.nombre, AC.email, AC.celular, AC.dia_hora_inicio, AC.dia_hora_termino, AC.descripcion, TE.nombre
            FROM actividad AC, comuna CO, tema TE
            WHERE AC.comuna_id=CO.id AND AC.tema_id=TE.id
            ORDER BY id DESC LIMIT 5;
            '''
        self.cursor.execute(sql)
        return self.cursor.fetchall()

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

    def get_actividad(self):
        sql = '''
        SELECT * FROM evento ORDER BY id DESC
        '''
        self.cursor.execute(sql)
        return self.cursor.fetchall()
    
    def get_actividad_por_date(self):
        sql ='''
        SELECT fecha, COUNT(fecha) 
        FROM (SELECT CAST(dia_hora_inicio AS date) as fecha FROM actividad AS f1) f1 
        GROUP BY fecha;
        '''
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        return data

    # def get_actividad_por_tema(self):
    #     sql ='''
    #     SELECT tema_id, COUNT(tema_id) 
    #     FROM (SELECT CAST(dia_hora_inicio AS date) as fecha FROM actividad AS f1) f1 
    #     GROUP BY fecha;
    #     '''
    #     self.cursor.execute(sql)
    #     data = self.cursor.fetchall()
    #     return data
    

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
        actividad = data[0]
        fotos = data[2]
        try:
            id_actividad = self.guardar_actividad(actividad)  # guarda la actividad y recupera el id
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

    def get_last_5(self):  # portada
        sql = '''
            SELECT AC.id, CO.nombre, AC.sector, AC.nombre, AC.email, AC.celular, AC.dia_hora_inicio, AC.dia_hora_termino, AC.descripcion, TE.nombre
            FROM actividad AC, comuna CO, tema TE
            WHERE AC.comuna_id=CO.id AND AC.tema_id=TE.id
            ORDER BY id DESC LIMIT 5;
            '''
        self.cursor.execute(sql)
        return self.cursor.fetchall()
