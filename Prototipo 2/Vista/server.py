from flask import *  # Se importa la librearia flask para levantar el servidor y manipular una WEB													# Se importa la libreria arxiv para utilizar el motor de busqueda que incorpora
from google import search
from lxml import html
from bs4 import BeautifulSoup
from readability import Document
import urllib
import os
import requests
import sys
import urlparse
import shutil
import pymysql.cursors


# Connect to the database
# connection = pymysql.connect(host='localhost',
#                             user='root',
#                             password='',
#                             db='FisFinder',
#                             charset='utf8mb4',
#                             cursorclass=pymysql.cursors.DictCursor)


def actualizar_Configuracion(datos):
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='',
                                 db='FisFinder',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)

    try:

        with connection.cursor() as cursor:
            # Create a new record
            sql = "UPDATE `Perfil` SET `Nro_IMG` = %s, `Nro_VIDEO` = %s, `Nro_ECC` = %s, `Nro_TEXTO` = %s, `Min_IMG` = %s, `Min_VIDEO` = %s, `Min_ECC` = %s, `Min_TEXTO` = %s WHERE `ID` = %s"
            cursor.execute(sql, datos)

        # connection is not autocommit by default. So you must commit to save
        # your changes.
        connection.commit()

    finally:
        connection.close()


def consultar_perfil(perfil="ASIMILADOR"):
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='',
                                 db='FisFinder',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)

    resultado = dict()
    try:

        # with connection.cursor() as cursor:
        # Create a new record
        # sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
        # cursor.execute(sql, ('webmaster@python.org', 'very-secret'))

        # connection is not autocommit by default. So you must commit to save
        # your changes.
        # connection.commit()

        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT `ID`, `Nro_IMG`, `Nro_VIDEO`, `Nro_ECC` , `Nro_TEXTO`, `Min_IMG`, `Min_VIDEO`, `Min_ECC`, `Min_TEXTO`  FROM `Perfil` WHERE `ID` = %s"
            cursor.execute(sql, perfil)
            result = cursor.fetchone()
            resultado = result
            print(result["Nro_IMG"])
            # Notar que result es un diccionario
            for i, j in result.items():
                print (i, j)
    finally:
        connection.close()

    return resultado


def consultar_datos(perfil):
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='',
                                 db='FisFinder',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)

    resultado = []
    try:

        # with connection.cursor() as cursor:
        # Create a new record
        # sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
        # cursor.execute(sql, ('webmaster@python.org', 'very-secret'))

        # connection is not autocommit by default. So you must commit to save
        # your changes.
        # connection.commit()

        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT `ID`, `Nro_IMG`, `Nro_VIDEO`, `Nro_ECC` , `Nro_TEXTO`, `Min_IMG`, `Min_VIDEO`, `Min_ECC`, `Min_TEXTO`  FROM `Perfil` WHERE `ID` = %s"
            cursor.execute(sql, perfil)
            result = cursor.fetchone()
            resultado.append(result["Nro_IMG"])
            resultado.append(result["Min_IMG"])
            resultado.append(result["Nro_VIDEO"])
            resultado.append(result["Min_VIDEO"])
            resultado.append(result["Nro_ECC"])
            resultado.append(result["Min_ECC"])
            resultado.append(result["Nro_TEXTO"])
            resultado.append(result["Min_TEXTO"])
            print(result["Nro_IMG"])
            # Notar que result es un diccionario
            for i, j in result.items():
                print (i, j)
    finally:
        connection.close()

    return resultado


def busqueda(user_spec, lista):
    resultados_busqueda = []
    i = 1
    j = 1
    shutil.rmtree("ISW")
    os.makedirs("ISW", 0755)
    for url in search(user_spec, tld='com', lang='es', stop=160):
        if i <= 10:
            print "--------------------"
            # Aqui estamos extrayendo_todo lo que necesitamos del HTML
            html = urllib.urlopen(url).read()
            titulo = Document(html).short_title()
            articulo = Document(html).summary()

            print str(i) + ". " + titulo
            print url
            print " "

            os.makedirs("ISW/" + str(i), 0755);
            arch = open("ISW/" + str(i) + ".txt", "w")
            arch2 = open("ISW/" + str(i) + ".html", "w")
            arch.write(articulo.encode('utf-8'))
            arch2.write(articulo.encode('utf-8'))
            arch.close()
            arch2.close()

            # Esta es la cosita para bajar imagenes :v
            """
            soup = BS(articulo)
            for imgtag in soup.find_all('img'):
                print(imgtag['src'])
                imagen_url = str ("http:" + imgtag['src'])
                nombre = imagen_url.rsplit('/',1)[1]
                print imagen_url
                urllib.urlretrieve(imagen_url, nombre)
            """

            # Aqui estamos viendo cuantas cosas tiene el HTML
            imagenes = 0
            videos = 0
            texto = 0
            arch = open("isw/" + str(i) + ".txt", "r")
            for linea in arch:
                if '<img' in linea:
                    imagenes = imagenes + 1
                if '<vid' in linea:
                    videos = videos + 1
                if '<p' in linea:
                    texto = texto + 1
            arch.close()
            print "Imagenes = " + str(imagenes)
            print "Videos = " + str(videos)
            print "Texto = " + str(texto)

            if (imagenes <= int(lista[0])) and (imagenes >= int(lista[1])) and (videos <= int(lista[2])) and (
                videos >= int(lista[3])) and (texto <= int(lista[6])) and (texto >= int(lista[7])):
                print "KOWABUNGA"
                resultados_busqueda.append((str(j) + ". " + titulo, url))
                j += 1
            i = i + 1
        else:
            break

    return resultados_busqueda


app = Flask(__name__)  # Se crea la clase aplicacion a mostrar en el navegador

app.secret_key = 'papas'


@app.route('/')  # Los elementos "route" definen las pestanias de la aplicacion
def default():  # Se define el inicio de la aplicacion
    if 'username' in session and 'password' in session:
        if session['username'] == 'admin' and session['password'] == '1234':
            username = session['username']
            return render_template('default.html',
                                   user=username)  # Se define default como la pagina de incicio de la aplicacion
    return render_template('login.html')


@app.route('/login', methods=['GET', 'POST'])  # Los elementos "route" definen las pestanias de la aplicacion
def login():  # Se define el inicio de la aplicacion
    if request.method == 'POST':
        session['username'] = request.form['username']
        session['password'] = request.form['password']
        return redirect(url_for('default'))


@app.route('/logout')
def logout():
    # remove the username from the session if it is there
    session.pop('username', None)
    return redirect(url_for('default.html'))


@app.route('/result', methods=['POST',
                               'GET'])  # La pestania "result" al ser accedida tomara los elementos enviados desde el origen
def result():
    if 'username' in session and 'password' in session:
        if session['username'] == 'admin' and session['password'] == '1234':
            if request.method == 'POST':  # Se verifica que tipo de paso de datos se ha utilizado
                busqueda_usuario = request.form['texto']
                tipo_aprendizaje = request.form['PERFIL']
                lista2 = consultar_datos(tipo_aprendizaje)
                try:
                    lista = busqueda(busqueda_usuario, lista2)
                    return render_template("result.html",
                                           result=lista)  # Se envian los datos a la pestania de resultados donde estos seran mostrados
                    # Por lo anterior se redirige al usuario a la pestania de resultados
                except:
                    return render_template("oye_tu.html")
    return render_template('login.html')
@app.route('/configuracion')
def configuracion():
    if 'username' in session and 'password' in session:
        if session['username'] == 'admin' and session['password'] == '1234':
            return render_template('configuracion.html')
    return render_template('login.html')


@app.route('/config_perfil', methods=['POST',
                                      'GET'])
def config_perfil():
    if 'username' in session and 'password' in session:
        if session['username'] == 'admin' and session['password'] == '1234':
            if request.method == 'POST':
                buscar = request.form['PERFIL']
                diccionario = consultar_perfil(buscar)
                lista = []
                lista.append(diccionario["ID"])
                lista.append(diccionario["Nro_IMG"])
                lista.append(diccionario["Nro_VIDEO"])
                lista.append(diccionario["Nro_ECC"])
                lista.append(diccionario["Nro_TEXTO"])
                lista.append(diccionario["Min_IMG"])
                lista.append(diccionario["Min_VIDEO"])
                lista.append(diccionario["Min_ECC"])
                lista.append(diccionario["Min_TEXTO"])
                return render_template('config_perfil.html', config_perfil=lista)
            else:
                lista = []
                lista.append("No Seleccionado")
                lista.append("")
                lista.append("")
                lista.append("")
                lista.append("")
                lista.append("")
                lista.append("")
                lista.append("")
                lista.append("")
                return render_template('config_perfil.html', config_perfil=lista)
    return render_template('login.html')


@app.route('/config_sitios')
def config_sitios():
    if 'username' in session and 'password' in session:
        if session['username'] == 'admin' and session['password'] == '1234':
            return render_template('config_sitios.html')
    return render_template('login.html')


@app.route('/respuesta_sitio', methods=['POST',
                                        'GET'])
def respuesta_sitio():
    if 'username' in session and 'password' in session:
        if session['username'] == 'admin' and session['password'] == '1234':
            if request.method == 'POST':
                lista = []
                lista.append(request.form["Nro_IMG"])
                lista.append(request.form["Nro_VIDEO"])
                lista.append(request.form["Nro_ECC"])
                lista.append(request.form["Nro_TEXTO"])
                lista.append(request.form["Min_IMG"])
                lista.append(request.form["Min_VIDEO"])
                lista.append(request.form["Min_ECC"])
                lista.append(request.form["Min_TEXTO"])
                lista.append(request.form["PERFIL_R"])

                actualizar_Configuracion(lista)

                respuesta = request.form['PERFIL_R']
                return render_template('respuesta_sitio.html', respuesta_sitio=respuesta)
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)
