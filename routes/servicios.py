from flask import Blueprint, render_template

servicios_bp = Blueprint("servicios", __name__)

@servicios_bp.route("/")
def servicios():
    return render_template("servicios.html")