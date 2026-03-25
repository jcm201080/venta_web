# 🚀 JCM Web Solutions

Página web profesional para la venta de páginas web y aplicaciones personalizadas.

---

## 🌐 Descripción

Este proyecto es una web comercial desarrollada con Flask que permite mostrar:

- Servicios de desarrollo web
- Planes y precios
- Portfolio con proyectos reales
- Formulario de contacto
- Chat con IA integrada
- Captura de conversaciones (leads)

---

## 🧠 Funcionalidades

✅ Landing page moderna  
✅ Sistema de rutas con Flask (Blueprints)  
✅ Chat interactivo con IA  
✅ Memoria por usuario (session)  
✅ Guardado de conversaciones en JSON  
✅ Diseño responsive  
✅ Integración con WhatsApp  

---

## 🧱 Estructura del proyecto
venta_web/
│
├── app.py
├── requirements.txt
├── .gitignore
├── conversaciones.json
│
├── ai/
│ └── simple_ai.py
│
├── routes/
│ ├── index.py
│ ├── servicios.py
│ ├── precios.py
│ ├── portfolio.py
│ ├── contacto.py
│
├── templates/
│ ├── base.html
│ ├── index.html
│ ├── servicios.html
│ ├── precios.html
│ ├── portfolio.html
│ ├── contacto.html
│
├── static/
│ ├── css/style.css
│ ├── js/chat.js
│ └── img/


---

## ⚙️ Instalación

```bash
git clone TU_REPO
cd venta_web

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt

▶️ Ejecutar en local
python app.py

Abrir en navegador:

http://127.0.0.1:5000
🤖 IA

El sistema incluye:

Chat con respuestas inteligentes
Memoria por usuario
Base preparada para integrar OpenAI o sistema de agentes
💾 Conversaciones

Las conversaciones se guardan en:

conversaciones.json

Permite analizar clientes potenciales.

🚀 Deploy

Preparado para desplegar en VPS con:

Gunicorn
Nginx
💡 Futuras mejoras
Guardado en base de datos
Panel de administración
IA con OpenAI
Sistema de leads avanzado
Multi-agentes
👨‍💻 Autor

Jesús Castaño
Desarrollo web + IA aplicada a negocio

## 🌍 Demo online

👉 https://webs.jesuscmweb.com