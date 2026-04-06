# routes/feria.py
from flask import Blueprint, render_template

feria_bp = Blueprint("feria", __name__)

@feria_bp.route("/feria")
def feria():
    return render_template("feria.html")