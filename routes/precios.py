from flask import Blueprint, render_template

precios_bp = Blueprint("precios", __name__)

@precios_bp.route("/")
def precios():
    return render_template("precios.html")