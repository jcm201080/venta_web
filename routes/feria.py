# routes/feria.py
from flask import Blueprint, render_template
from utils.visitas import registrar_visita

feria_bp = Blueprint("feria", __name__)

@feria_bp.route("/feria")
def feria():
    registrar_visita(origen="feria")
    return render_template("feria.html")  # o feria.html