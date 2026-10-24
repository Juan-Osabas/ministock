from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

@app.route("/saludo")
def saludo():
    return "Hola MiniStock"

@app.route("/clave")
def clave():
    return f"clave cargada: {bool(app.config['SECRET_KEY'])}"

if __name__ == "__main__":
    app.run()