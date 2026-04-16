from flask import Blueprint, render_template
from utils.visitas import registrar_visita

nfc_bp = Blueprint("nfc", __name__)

@nfc_bp.route("/nfc/demo")
def nfc_demo():
    registrar_visita(origen="nfc")

    return render_template("nfc_demo.html")