from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def login():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def verificar_login():

    usuario = request.form.get("usuario")
    password = request.form.get("password")

    if usuario == "admin" and password == "1234":
        return render_template("dashboard.html", usuario=usuario)
    else:

        return render_template("login.html", error="Credenciales incorrectas")

if __name__ == "__main__":
    app.run(debug=True)