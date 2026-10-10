import os
import shutil

# 1. Pastikan folder public ada
os.makedirs('public', exist_ok=True)

# 2. Salin index.html utama agar tersedia di root dan public (untuk antisipasi berbagai konfigurasi GitHub Pages)
if os.path.exists('index.html'):
    shutil.copy('index.html', 'public/index.html')

print("Struktur folder siap di-push.")
