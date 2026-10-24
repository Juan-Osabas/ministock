from flask import Flask
from config import Config
from models import db
from flask import render_template
from models import db, Categoria, Producto
from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)
app.config.from_object(Config)


@app.route("/productos")
def productos():
     productos = Producto.query.all()
     return render_template("productos.html", productos = productos)

@app.route("/productos/nuevos", methods=["GET", "POST"])
def nuevos_productos():
    if request.method == "POST":
        nombre = request.form["nombre"]
        precio = float(request.form["precio"])
        stock = int(request.form["stock"])
        descripcion = request.form["descripcion"]
        categoria_id = int(request.form["categoria_id"])

        producto = Producto(
            nombre=nombre,
            precio=precio,
            stock=stock,
            descripcion=descripcion,
            categoria_id=categoria_id
        )
        db.session.add(producto)
        db.session.commit()
        return redirect(url_for("productos"))

    categorias = Categoria.query.all()
    return render_template("nuevos_productos.html", categorias = categorias)

db.init_app(app)
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run()