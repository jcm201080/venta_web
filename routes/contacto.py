from flask import Blueprint, render_template, request, redirect, url_for, flash
import smtplib
from email.mime.text import MIMEText
import os

contacto_bp = Blueprint("contacto", __name__)

@contacto_bp.route("/", methods=["GET", "POST"])
def contacto():
    if request.method == "POST":
        nombre = request.form.get("nombre")
        email = request.form.get("email")
        mensaje = request.form.get("mensaje")

        # 📧 contenido del email
        contenido = f"""
Nuevo contacto desde tu web:

👤 Nombre: {nombre}
📧 Email: {email}

💬 Mensaje:
{mensaje}
        """

        msg = MIMEText(contenido)
        msg["Subject"] = "Nuevo cliente desde la web 🚀"
        msg["From"] = os.getenv("EMAIL_USER")
        msg["To"] = os.getenv("EMAIL_USER")

        # 👉 opcional pero PRO
        msg["Reply-To"] = email

        try:
            servidor = smtplib.SMTP("smtp.gmail.com", 587)
            servidor.starttls()

            servidor.login(
                os.getenv("EMAIL_USER"),
                os.getenv("EMAIL_PASS")
            )

            servidor.send_message(msg)
            servidor.quit()

            flash("Mensaje enviado correctamente 🚀")

        except Exception as e:
            print("Error enviando email:", e)
            flash("Error al enviar el mensaje ❌")

        return redirect(url_for("contacto.contacto"))

    return render_template("contacto.html")