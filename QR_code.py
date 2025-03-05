import qrcode
from PIL import Image

# Generate QR code
qr = qrcode.QRCode(version=1,
                   error_correction = qrcode.ERROR_CORRECT_H,
                   box_size=10,border=4)
qr.add_data("https://www.boostupdigital.in/")
qr.make(fit=True)

# Create QR image
img= qr.make_image(fill_color="black",back_color="white")

# Open the logo image 
logo = Image.open("QR_code.py/boostUp_logo.jfif")
logo = logo.convert("RGBA")

# Resize the logo
logo_size = 80  
logo = logo.resize((logo_size, logo_size))

# Get QR code size and calculate center position
qr_width, qr_height = img.size
logo_position = ((qr_width - logo_size) // 2, (qr_height - logo_size) // 2)

# Paste the logo onto the QR code
img = img.convert("RGBA")
img.paste(logo, logo_position, logo if logo.mode == "RGBA" else None)

# Save the image 
img.save("boostup_digital.png")