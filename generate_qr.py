import sys
import os
import qrcode
from PIL import Image

def generate_watertree_qr(target_url="http://127.0.0.1:5000", output_filename="static/qr_code.png"):
    """
    Generates a high-resolution, branded QR code pointing to the gym equipment portal.
    Uses Watertree Deep Teal (#0A3C42) on a crisp white background.
    """
    os.makedirs(os.path.dirname(output_filename), exist_ok=True)

    # Configure QR code with High error correction (allows logo overlay or minor wear)
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=12,
        border=3,
    )
    qr.add_data(target_url)
    qr.make(fit=True)

    # Color matching Watertree Deep Teal (#0A3C42) and pure white background
    img = qr.make_image(
        fill_color="#0A3C42",
        back_color="#FFFFFF"
    ).convert('RGB')

    img.save(output_filename, format="PNG")
    print(f"✓ QR Code successfully generated pointing to: {target_url}")
    print(f"✓ Saved to: {output_filename}")

if __name__ == "__main__":
    # If a URL is passed via terminal: python generate_qr.py https://my-gym-portal.onrender.com
    url = sys.argv[1] if len(sys.argv) > 1 else "http://127.0.0.1:5000"
    generate_watertree_qr(url)