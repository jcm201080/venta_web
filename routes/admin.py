from flask import Blueprint, render_template
import sqlite3
from flask import request, abort

ADMIN_PASSWORD = "4812"  # cámbiala

admin_bp = Blueprint("admin", __name__)

@admin_bp.route("/admin/visitas")
def ver_visitas():
    password = request.args.get("key")

    if password != ADMIN_PASSWORD:
        abort(403)

    conn = sqlite3.connect('visitas.db')
    cursor = conn.cursor()

    # 🔹 total visitas
    cursor.execute("SELECT COUNT(*) FROM visitas WHERE origen='feria'")
    total = cursor.fetchone()[0]

    # 🔹 últimos 7 días
    cursor.execute("""
        SELECT DATE(fecha), COUNT(*)
        FROM visitas
        WHERE origen='feria'
        AND fecha >= datetime('now', '-7 days')
        GROUP BY DATE(fecha)
        ORDER BY DATE(fecha)
    """)
    datos_7dias = cursor.fetchall()

    # 🔹 IPs únicas
    cursor.execute("""
        SELECT COUNT(DISTINCT ip)
        FROM visitas
        WHERE origen='feria'
    """)
    ips_unicas = cursor.fetchone()[0]

    # clic en wasap
    cursor.execute("SELECT COUNT(*) FROM visitas WHERE origen='whatsapp'")
    whatsapp = cursor.fetchone()[0]

    # 🔹 visitas por página (total)
    cursor.execute("""
        SELECT ruta, COUNT(*) 
        FROM visitas
        WHERE origen='web'
        GROUP BY ruta
        ORDER BY COUNT(*) DESC
    """)
    paginas_total = cursor.fetchall()

    # 🔹 visitas por página últimas 24h
    cursor.execute("""
        SELECT ruta, COUNT(*) 
        FROM visitas
        WHERE origen='web'
        AND fecha >= datetime('now', '-1 day')
        GROUP BY ruta
        ORDER BY COUNT(*) DESC
    """)
    paginas_24h = cursor.fetchall()

    conn.close()

    return render_template(
        "admin/visitas.html",
        total=total,
        datos_7dias=datos_7dias,
        ips_unicas=ips_unicas,
        whatsapp=whatsapp,
        paginas_total=paginas_total,
        paginas_24h=paginas_24h
    )


from utils.visitas import registrar_visita
from flask import redirect

@admin_bp.route("/track_whatsapp")
def track_whatsapp():
    registrar_visita(origen="whatsapp")
    return redirect("https://wa.me/34614398084")  # tu número



