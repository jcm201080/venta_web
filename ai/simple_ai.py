from config import PRECIOS

import os
import json

def generar_respuesta(contexto):
    ultimo = contexto[-1]["content"].lower()

    basico = PRECIOS["basico"]
    pro = PRECIOS["profesional"]
    premium = PRECIOS["premium"]

    # 💰 PRECIOS (mejorado)
    if any(p in ultimo for p in ["precio", "cuanto", "coste"]):
        return (
            f"Te explico las opciones más habituales 👇\n\n"

            f"🟢 Web básica ({basico})\n"
            "Para empezar rápido y tener presencia online.\n\n"

            f"🟡 Web profesional ({pro})\n"
            "La opción más elegida para negocios activos.\n\n"

            f"🔴 Web con IA ({premium})\n"
            "Automatiza tu negocio y ahorra tiempo.\n\n"

            "💡 El precio es orientativo según lo que necesites.\n\n"

            "👉 Si me dices tu negocio, te recomiendo la mejor opción 😉"
        )

    # 🎯 QUIERE WEB
    elif any(p in ultimo for p in ["quiero web", "pagina web", "hacer web"]):
        return (
            "Perfecto 🚀 vamos a hacerlo fácil:\n\n"
            "1️⃣ ¿Qué tipo de negocio tienes?\n"
            "2️⃣ ¿Qué quieres conseguir? (clientes, reservas, ventas...)\n\n"
            "👉 Con eso te recomiendo la mejor opción sin complicaciones."
        )

    # 🧠 NEGOCIO DETECTADO
    elif any(p in ultimo for p in ["negocio", "tengo", "soy"]):
        return (
            "Genial 🔥 eso tiene mucho potencial.\n\n"

            f"👉 Empezar rápido → web básica ({basico})\n"
            f"👉 Gestionar clientes → web profesional ({pro})\n"
            f"👉 Automatizar → web con IA ({premium})\n\n"

            "👉 ¿Qué te gustaría mejorar ahora mismo?"
        )

    # 🤖 IA
    elif "ia" in ultimo:
        return (
            "La IA convierte tu web en un asistente automático 🤖\n\n"
            "✔ Responde clientes\n"
            "✔ Explica tus servicios\n"
            "✔ Puede gestionar reservas o pedidos\n\n"
            "👉 Ideal si quieres ahorrar tiempo y no perder oportunidades."
        )

    # ⏱ TIEMPO
    elif any(p in ultimo for p in ["tiempo", "tarda", "dias"]):
        return (
            "Trabajamos rápido 🚀\n\n"
            "🟢 Básica → 1-2 días\n"
            "🟡 Profesional → 3-5 días\n"
            "🔴 IA → 5-7 días\n\n"
            "👉 Siempre intentamos entregarlo lo antes posible."
        )
    elif any(p in ultimo for p in ["presupuesto", "precio exacto", "cuanto vale", "cuanto seria"]):
        return (
            "Perfecto 👌\n\n"
            "Para darte un precio exacto necesito saber:\n\n"
            "👉 Tipo de negocio\n"
            "👉 Qué necesitas (web, reservas, tienda...)\n\n"
            "Puedes decírmelo aquí o escribirme directamente por WhatsApp 📲"
        )
    # 🎯 RECOMENDACIÓN AUTOMÁTICA
    elif any(p in ultimo for p in ["restaurante", "bar", "cafeteria"]):
        return (
            "Perfecto 🍔\n\n"
            "Para un restaurante te recomiendo:\n\n"
            f"👉 Web profesional ({pro})\n"
            "Porque podrás gestionar menú, clientes o pedidos.\n\n"
            "👉 Si quieres automatizar reservas o pedidos → plan con IA.\n\n"
            "¿Quieres algo sencillo o más completo?"
        )

    elif any(p in ultimo for p in ["peluqueria", "barberia", "estetica"]):
        return (
            "Genial 💇‍♂️\n\n"
            "Lo ideal para tu caso:\n\n"
            f"👉 Web profesional ({pro})\n"
            "Para gestionar citas y servicios.\n\n"
            "👉 Con IA puedes automatizar reservas.\n\n"
            "¿Quieres que los clientes puedan reservar solos?"
        )

    elif any(p in ultimo for p in ["tienda", "vender", "productos"]):
        return (
            "Perfecto 🛒\n\n"
            "Para vender online necesitas:\n\n"
            f"👉 Web profesional ({pro}) o superior\n"
            "Para gestionar productos y pedidos.\n\n"
            "👉 Si quieres automatizar ventas → plan con IA.\n\n"
            "¿Qué tipo de productos vendes?"
        )

    elif any(p in ultimo for p in ["recomienda", "que plan", "cual elegir"]):
        return (
            "Te lo pongo fácil 👇\n\n"
            f"👉 Empezar → Básico ({basico})\n"
            f"👉 Negocio activo → Profesional ({pro})\n"
            f"👉 Automatizar → IA ({premium})\n\n"
            "👉 Si me dices qué negocio tienes, te digo exactamente cuál elegir 😉"
        )

    elif any(p in ultimo for p in ["no se", "no tengo claro", "duda"]):
        return (
            "No te preocupes 👌\n\n"
            "Te ayudo a elegir la mejor opción según tu caso.\n\n"
            "👉 ¿A qué te dedicas?"
        )

    # 💬 CIERRE (MUY IMPORTANTE)
    else:
        return (
            "Cuéntame un poco sobre tu negocio 😊\n\n"

            "👉 ¿A qué te dedicas?\n"
            "👉 ¿Quieres captar clientes, vender o automatizar?\n\n"

            "Y te digo exactamente qué necesitas 👌"
        )



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


