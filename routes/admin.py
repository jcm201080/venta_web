from flask import Blueprint, render_template
import sqlite3
from flask import request, abort

ADMIN_PASSWORD = "4812"

admin_bp = Blueprint("admin", __name__)

@admin_bp.route("/admin/visitas")
def ver_visitas():
    password = request.args.get("key")

    if password != ADMIN_PASSWORD:
        abort(403)

    conn = sqlite3.connect('visitas.db')
    cursor = conn.cursor()

    # 🔥 TOTAL VISITAS (TODAS)
    cursor.execute("SELECT COUNT(*) FROM visitas")
    total = cursor.fetchone()[0]

    # 🔥 VISITAS POR ORIGEN (web, feria, whatsapp)
    cursor.execute("""
        SELECT origen, COUNT(*) 
        FROM visitas
        GROUP BY origen
    """)
    origenes = cursor.fetchall()

    # 🔹 últimos 7 días (SOLO FERIA)
    cursor.execute("""
        SELECT DATE(fecha), COUNT(*)
        FROM visitas
        WHERE origen='feria'
        AND fecha >= datetime('now', '-7 days')
        GROUP BY DATE(fecha)
        ORDER BY DATE(fecha)
    """)
    datos_7dias = cursor.fetchall()

    # 🔹 IPs únicas (FERIA)
    cursor.execute("""
        SELECT COUNT(DISTINCT ip)
        FROM visitas
        WHERE origen='feria'
    """)
    ips_unicas = cursor.fetchone()[0]

    # 🔹 clics en WhatsApp
    cursor.execute("SELECT COUNT(*) FROM visitas WHERE origen='whatsapp'")
    whatsapp = cursor.fetchone()[0]

    # 🔥 VISITAS POR PÁGINA (LIMPIO)
    cursor.execute("""
        SELECT ruta, COUNT(*) 
        FROM visitas
        WHERE origen='web'
        AND ruta NOT LIKE '/api%'
        AND ruta NOT LIKE '/static%'
        AND ruta NOT LIKE '%favicon%'
        GROUP BY ruta
        ORDER BY COUNT(*) DESC
    """)
    paginas_total = cursor.fetchall()

    # 🔹 últimas 24h
    cursor.execute("""
        SELECT ruta, COUNT(*) 
        FROM visitas
        WHERE origen='web'
        AND fecha >= datetime('now', '-1 day')
        AND ruta NOT LIKE '/api%'
        AND ruta NOT LIKE '/static%'
        AND ruta NOT LIKE '%favicon%'
        GROUP BY ruta
        ORDER BY COUNT(*) DESC
    """)
    paginas_24h = cursor.fetchall()

    # 🔥 COMBINAR DATOS (MUY IMPORTANTE)
    paginas_dict_24h = dict(paginas_24h)

    paginas = []
    for ruta, total_visitas in paginas_total:
        ultimas = paginas_dict_24h.get(ruta, 0)
        paginas.append((ruta, total_visitas, ultimas))

    conn.close()

    return render_template(
        "admin/visitas.html",
        total=total,
        datos_7dias=datos_7dias,
        ips_unicas=ips_unicas,
        whatsapp=whatsapp,
        paginas=paginas,
        origenes=origenes
    )


from utils.visitas import registrar_visita
from flask import redirect

@admin_bp.route("/track_whatsapp")
def track_whatsapp():
    msg = request.args.get("msg", "Hola, quiero información")
    ruta = request.referrer or "directo"

    registrar_visita(origen="whatsapp", ruta=ruta)

    return redirect(f"https://wa.me/34614398084?text={msg}")