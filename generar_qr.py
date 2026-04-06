import qrcode
from qrcode.constants import ERROR_CORRECT_H

qr = qrcode.QRCode(
    version=1,
    error_correction=ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

qr.add_data("https://creacion.jesuscmweb.com/feria")
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")

img.save("qr_feria.png")

print("QR generado en qr_feria.png ✅")
