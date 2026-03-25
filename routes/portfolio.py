from flask import Blueprint, render_template
import os

portfolio_bp = Blueprint("portfolio", __name__)

# 📁 Rutas
RUTA_TEMPLATES = os.path.join("templates", "basicas")
RUTA_IMAGENES = os.path.join("static", "img", "basicas")


@portfolio_bp.route("/")
def portfolio():

    basicas = []

    try:
        archivos = os.listdir(RUTA_TEMPLATES)

        for f in archivos:
            if f.endswith(".html"):

                nombre = f.replace(".html", "")

                # 🖼️ comprobar imagen
                img_jpg = os.path.join(RUTA_IMAGENES, nombre + ".jpg")
                img_png = os.path.join(RUTA_IMAGENES, nombre + ".png")

                if os.path.exists(img_jpg):
                    img = nombre + ".jpg"
                elif os.path.exists(img_png):
                    img = nombre + ".png"
                else:
                    img = "default.jpg"  # 👈 fallback

                basicas.append({
                    "archivo": f,
                    "nombre": nombre,
                    "img": img
                })

    except Exception as e:
        print("❌ Error cargando portfolio:", e)

    return render_template("portfolio.html", basicas=basicas)


@portfolio_bp.route("/basicas/<nombre>")
def ver_basica(nombre):

    try:
        # 🔒 seguridad básica (evitar rutas raras)
        if not nombre.endswith(".html"):
            return "Ruta no válida", 400

        ruta = os.path.join(RUTA_TEMPLATES, nombre)

        if not os.path.exists(ruta):
            return "Plantilla no encontrada", 404

        return render_template(f"basicas/{nombre}")

    except Exception as e:
        print("❌ Error cargando plantilla:", e)
        return "Error interno", 500