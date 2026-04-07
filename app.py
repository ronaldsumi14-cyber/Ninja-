from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/")
def home():
    cadena = "Texto de prueba"
    nombre = "Pepe"
    return render_template("index.html", content="Probando variables", contenido=cadena, nombre = nombre)

if __name__== "__main__":
    app.run(debug=True)