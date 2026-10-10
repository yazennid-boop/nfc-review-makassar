from PIL import Image, ImageDraw, ImageFont
import os

# Membuat placeholder nfc-card.jpg
img_card = Image.new('RGB', (800, 500), color=(15, 23, 42))
d_card = ImageDraw.Draw(img_card)
d_card.rectangle([40, 40, 760, 460], outline=(66, 133, 244), width=4)
d_card.text((100, 200), "NFC GOOGLE REVIEW", fill=(255, 255, 255))
d_card.text((100, 250), "Makassar - Tap & Go", fill=(96, 165, 250))
img_card.save('nfc-card.jpg')

# Membuat placeholder qris.jpg
img_qris = Image.new('RGB', (500, 500), color=(255, 255, 255))
d_qris = ImageDraw.Draw(img_qris)
d_qris.rectangle([50, 50, 450, 450], outline=(0, 0, 0), width=6)
d_qris.text((120, 220), "QRIS RESMI", fill=(0, 0, 0))
d_qris.text((100, 260), "Scan untuk Pembayaran", fill=(100, 100, 100))
img_qris.save('qris.jpg')

print("Placeholder gambar berhasil dibuat.")
