from flask import *														# Se importa la librearia flask para levantar el servidor y manipular una WEB
from arxiv import *														# Se importa la libreria arxiv para utilizar el motor de busqueda que incorpora
app = Flask(__name__)													# Se crea la clase aplicacion a mostrar en el navegador


@app.route('/')															# Los elementos "route" definen las pestanias de la aplicacion
def login():															# Se define el inicio de la aplicacion
   return render_template('default.html')								# Se define default como la pagina de incicio de la aplicacion

@app.route('/result',methods = ['POST', 'GET'])							# La pestania "result" al ser accedida tomara los elementos enviados desde el origen
def result():
   if request.method == 'POST':											# Se verifica que tipo de paso de datos se ha utilizado
      texto= request.form['texto']										# Se almacena lo que ha ingresado el usuario para buscar
      maximo = 10;														# Se fija el numero de resultados a 10 de estos
      #maximo = request.form['maximo']									# Si fuese el caso, se podria tomar el numero de resultados que el usuario escoja
      a= arxiv.query( texto, prune=True, start=0, max_results = maximo) # Se utiliza metodo de la libreria arxiv para buscar en dicho sistema lo que el usuario a solicitado
      d={}																# Se crean diccionarios para enviar datos a la pestania de resultados, para mostrarlos
      d2={}
      for i in range(0, len(a)):										# Se guardan en los diccionarios los datos que se mostraran en resultados
         b= a[i]														# extraidos desde arxiv mediante el metodo que provee la libreria
         d2[b['pdf_url']] = b['summary']
         d[b['pdf_url']] = b['title']
      lista=[d,d2]
      return render_template("result.html",result = lista)				# Se envian los datos a la pestania de resultados donde estos seran mostrados
																		# Por lo anterior se redirige al usuario a la pestania de resultados
if __name__ == '__main__':
   app.run(debug = True)



