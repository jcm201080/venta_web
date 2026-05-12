import os
import json
from openai import OpenAI
from config import PRECIOS
from dotenv import load_dotenv

# Importamos el cerebro desde el nuevo archivo
from ai.prompts import PROMPT_VENDEDOR_ESTRELLA

# Cargar variables de entorno
load_dotenv()
API_KEY = os.getenv("OPENAI_API_KEY")

if API_KEY:
    client = OpenAI(api_key=API_KEY)
else:
    client = None

# ==========================================
# 🛡️ SISTEMA DE RESPALDO (GRATUITO)
# ==========================================
def respuesta_gratuita_basica(contexto):
    ultimo_mensaje = contexto[-1]["content"].lower()
    basico = PRECIOS["basico"]
    pro = PRECIOS["profesional"]
    premium = PRECIOS["premium"]

    if any(p in ultimo_mensaje for p in ["precio", "cuanto", "coste", "caro"]):
        return f"Podemos ser flexibles 😊.\nTenemos el Básico ({basico}), Profesional ({pro}) o Premium con IA ({premium}).\nSi se te va de presupuesto, déjame tu WhatsApp y miramos qué podemos ajustarte. ¿Te parece?"
    
    elif any(p in ultimo_mensaje for p in ["peluqueria", "barberia", "estetica", "demo", "ejemplo"]):
        return f"¡Genial! 💇‍♂️ Tenemos el plan Profesional ({pro}) que es brutal.\nMira esta demo funcionando real: https://peluqueria-demo.jesuscmweb.com/ \n¿Te gustaría algo así para tu negocio?"
    
    else:
        return "¡Hola! Cuéntame un poco sobre tu negocio 😊\n👉 ¿A qué te dedicas?\n👉 ¿Quieres captar clientes, vender o gestionar reservas?\nTe diré exactamente qué necesitas 👌"

# ==========================================
# 🧠 GENERADOR DE RESPUESTAS (INTENTA IA PRIMERO)
# ==========================================
def generar_respuesta(contexto):
    if not client:
        return respuesta_gratuita_basica(contexto)

    mensajes_api = [{"role": "system", "content": PROMPT_VENDEDOR_ESTRELLA}]
    for msg in contexto:
        mensajes_api.append({"role": msg["role"], "content": msg["content"]})

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=mensajes_api,
            temperature=0.7,
            max_tokens=300
        )
        return response.choices[0].message.content

    except Exception as e:
        print(f"❌ Error con OpenAI ({e}). Activando sistema de respaldo.")
        return respuesta_gratuita_basica(contexto)

# ==========================================
# 💾 GUARDADO DE CONVERSACIONES
# ==========================================
def guardar_conversacion(user_id, mensaje, respuesta):
    archivo = "conversaciones.json"
    data = []
    if os.path.exists(archivo):
        try:
            with open(archivo, "r", encoding="utf-8") as f:
                data = json.load(f)
        except json.JSONDecodeError:
            pass 
    data.append({
        "user_id": user_id,
        "mensaje": mensaje,
        "respuesta": respuesta
    })
    with open(archivo, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)