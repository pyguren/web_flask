from flask import Flask, render_template
# guardamos el objeto que nos devuelve flask en una variable llamada app, la cual
# nos servira para poder crear nuestras rutas del servidor y url
app = Flask(__name__)
# Para crear una ruta tenemos que utilizar un decorador (@) y app y el metodo "route"
# se coloca un slash dentro del parentesis para señalar que esta sera la pagina principal


@app.route('/')
# ruta para pagina principal
# creo una funcion llamada home y esta nos va a retornar un texto cuando el
# usuario entre al home
def home():
    return render_template('inicio.html')


@app.route('/about')
def about():
    return render_template('servicios.html')

# hacemos una validacion para confirmar que estamos ejecutando un archivo de ejecucion
# y no un modulo, esto es mas que todo para que el servidor este el 100% del tiempo
# escuchando por si hay alguna peticion


@app.route('/contact')
def contact():
    return render_template('contacto.html')


# aca le indicamos cual es el archivo que va a arrancar nuestra aplicacion
if __name__ == '__main__':
    app.run(debug=True)

# se guarda y se ejecuta en la terminal usando localhost
