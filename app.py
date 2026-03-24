from flask import Flask, request, jsonify, session
import uuid
import json
import os

app = Flask(__name__)
app.secret_key = "clave_super_secreta_123"

# 🔹 IMPORTAR RUTAS
from routes.index import index_bp
from routes.servicios import servicios_bp
from routes.precios import precios_bp
from routes.portfolio import portfolio_bp
from routes.contacto import contacto_bp

# 🔹 IA
from ai.simple_ai import generar_respuesta, guardar_conversacion

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


# 🔹 REGISTRAR BLUEPRINTS
app.register_blueprint(index_bp)
app.register_blueprint(servicios_bp, url_prefix="/servicios")
app.register_blueprint(precios_bp, url_prefix="/precios")
app.register_blueprint(portfolio_bp, url_prefix="/portfolio")
app.register_blueprint(contacto_bp, url_prefix="/contacto")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8015, debug=True)