from flask import Flask, render_template
import pymysql

""" RUTAS """
app=Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/buscar-receta")
def buscar_receta():
    return render_template('buscar_receta.html')

@app.route("/cambiar-premuim")
def cambiar_premuim():
    return render_template('cambiar_premuim.html')

@app.route("/contactanos-usuarios")
def contactanos_usuarios():
    return render_template('contactanos_usuarios.html')

@app.route("/contactanos")
def contactanos():
    return render_template('contactanos.html')

@app.route("/crear-receta")
def crear_receta():
    return render_template('crear_receta.html')

@app.route("/home-cocinero")
def home_cocinero():
    return render_template('home_cocinero.html')

@app.route("/home-nutricionista")
def home_nutricionista():
    return render_template('home_nutricionista.html')

@app.route("/home-usuario")
def home_usuario():
    return render_template('home_usuario.html')

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/mensajeria")
def mensajeria():
    return render_template('mensajeria.html')

@app.route("/olvido-contraseña")
def olvido_contraseña():
    return render_template('olvido_contraseña.html')

@app.route("/quienes-somos")
def quienes_somos():
    return render_template('quienes_somos.html')

@app.route("/preguntas-frecuentes")
def preguntas_frecuentes():
    return render_template('preguntas_frecuentes.html')

@app.route("/registro")
def registro():
    return render_template('registro.html')

@app.route("/terminos-condiciones")
def terminos_condiciones():
    return render_template('terminos_condiciones.html')



if __name__=="__main__":
    app.run(debug=True)



