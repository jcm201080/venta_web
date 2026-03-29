import qrcode
import os

def generar_qr():
    url = "https://creacion.jesuscmweb.com/"

    ruta = os.path.join("static", "img", "qr_jcm.png")

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )

    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(ruta)

    print(f"QR generado en {ruta}")