from flask import Flask, request, jsonify, session
import uuid
import json
import os

from utils.visitas import inicializar_db
from config import PRECIOS

from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
app.secret_key = "clave_super_secreta_123"
app.config["PRECIOS"] = PRECIOS

# 🔥 INICIALIZAR BD DE VISITAS
inicializar_db()

# 🔹 IMPORTAR RUTAS
from routes.index import index_bp
from routes.servicios import servicios_bp
from routes.precios import precios_bp
from routes.portfolio import portfolio_bp
from routes.contacto import contacto_bp
from routes.feria import feria_bp
from routes.admin import admin_bp
# 🔹 IA
from ai.simple_ai import generar_respuesta, guardar_conversacion

from utils.visitas import registrar_visita
from flask import request

@app.before_request
def track_all():
    if (
        request.path.startswith("/static") or
        request.path.startswith("/admin") or
        request.path.startswith("/track")
    ):
        return

    # 🔥 SOLO UNA VEZ POR SESIÓN
    if not session.get("visitado"):
        session["visitado"] = True
        origen = detectar_origen()
        registrar_visita(origen=origen)

def detectar_origen():
    origen_param = request.args.get("origen")

    if origen_param:
        return origen_param

    ref = request.referrer

    if ref:
        if "wa.me" in ref:
            return "whatsapp"

    return "web"

# 🧠 MEMORIA EN SERVIDOR
memoria = {}


@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        mensaje = data.get("mensaje", "").strip()

        if not mensaje:
            return jsonify({"respuesta": "Escribe algo 😊"})

        # 🔹 sesión usuario
        if "user_id" not in session:
            session["user_id"] = str(uuid.uuid4())

        user_id = session["user_id"]

        # 🔹 inicializar memoria
        if user_id not in memoria:
            memoria[user_id] = []

        # guardar mensaje usuario
        memoria[user_id].append({"role": "user", "content": mensaje})

        # 🔥 CONTEXTO
        contexto = memoria[user_id][-5:]

        # 🧠 IA
        respuesta = generar_respuesta(contexto)

        # 💾 guardar conversación
        guardar_conversacion(user_id, mensaje, respuesta)

        # guardar respuesta
        memoria[user_id].append({"role": "assistant", "content": respuesta})

        return jsonify({"respuesta": respuesta})

    except Exception as e:
        print("❌ Error en /chat:", e)
        return jsonify({"respuesta": "Ha habido un error, prueba de nuevo o escríbeme por WhatsApp 📲"})

@app.context_processor
def inject_precios():
    return dict(precios=app.config["PRECIOS"])


# 🔹 REGISTRAR BLUEPRINTS
app.register_blueprint(index_bp)
app.register_blueprint(servicios_bp, url_prefix="/servicios")
app.register_blueprint(precios_bp, url_prefix="/precios")
app.register_blueprint(portfolio_bp, url_prefix="/portfolio")
app.register_blueprint(contacto_bp, url_prefix="/contacto")
app.register_blueprint(feria_bp)
app.register_blueprint(admin_bp)



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8015, debug=True)
    