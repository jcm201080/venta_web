from flask import Blueprint, render_template, request, redirect, url_for

contacto_bp = Blueprint("contacto", __name__)

@contacto_bp.route("/", methods=["GET", "POST"])
def contacto():
    if request.method == "POST":
        nombre = request.form.get("nombre")
        email = request.form.get("email")
        mensaje = request.form.get("mensaje")

        # 🔥 De momento solo lo mostramos por consola
        print(f"Nuevo contacto: {nombre} - {email} - {mensaje}")

        return redirect(url_for("contacto.contacto"))

    return render_template("contacto.html")