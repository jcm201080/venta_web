def generar_respuesta(contexto):
    ultimo = contexto[-1]["content"].lower()

    # 💰 PRECIOS
    if any(p in ultimo for p in ["precio", "cuanto", "coste"]):
        return (
            "Te explico las opciones de forma clara:\n\n"
            "🟢 Web básica (150€)\n"
            "Perfecta si quieres empezar. Incluye una página moderna con información de tu negocio, contacto y WhatsApp.\n\n"
            "🟡 Web profesional (350€)\n"
            "Aquí ya tienes control total: base de datos, panel de administración y puedes modificar tu contenido fácilmente.\n\n"
            "🔴 Web con IA (600€+)\n"
            "Automatiza tu negocio: la web responde a tus clientes, gestiona reservas o pedidos y trabaja por ti 24/7.\n\n"
            "👉 Cuéntame qué tipo de negocio tienes y te recomiendo la mejor opción."
        )

    # 🧠 CLIENTE CON NEGOCIO
    elif any(p in ultimo for p in ["negocio", "tengo", "soy"]):
        return (
            "Genial 🔥 eso tiene mucho potencial.\n\n"
            "Dependiendo de lo que quieras conseguir:\n\n"
            "👉 Más visibilidad → web básica\n"
            "👉 Gestionar clientes/productos → web profesional\n"
            "👉 Automatizar trabajo → web con IA\n\n"
            "Cuéntame qué te gustaría mejorar y te guío paso a paso."
        )

    # 🤖 IA
    elif "ia" in ultimo:
        return (
            "La IA en tu web es como tener un asistente digital:\n\n"
            "✔ Responde a tus clientes automáticamente\n"
            "✔ Explica tus servicios\n"
            "✔ Puede gestionar reservas o pedidos\n\n"
            "👉 Así no pierdes clientes aunque no estés disponible 😄"
        )

    # ⏱ TIEMPO
    elif any(p in ultimo for p in ["tiempo", "tarda", "dias"]):
        return (
            "Normalmente trabajamos así:\n\n"
            "🟢 Web básica → 1-2 días\n"
            "🟡 Profesional → 3-5 días\n"
            "🔴 IA → 5-7 días\n\n"
            "Siempre intentamos entregarlo lo antes posible 🚀"
        )

    # 🎯 DEFAULT (IMPORTANTE → vender)
    else:
        return (
            "Cuéntame qué necesitas 😊\n\n"
            "Por ejemplo:\n"
            "👉 'quiero una web para mi negocio'\n"
            "👉 'cuánto cuesta'\n"
            "👉 'qué incluye cada plan'\n\n"
            "Y te explico todo paso a paso."
        )


import json
import os



def guardar_conversacion(user_id, mensaje, respuesta):
    archivo = "conversaciones.json"

    data = []

    if os.path.exists(archivo):
        with open(archivo, "r") as f:
            data = json.load(f)

    data.append({
        "user_id": user_id,
        "mensaje": mensaje,
        "respuesta": respuesta
    })

    with open(archivo, "w") as f:
        json.dump(data, f, indent=4)