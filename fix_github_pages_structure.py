import shutil
import os

# Memastikan direktori public ada dan menyalin index.html ke root agar langsung dibaca GitHub Pages
if os.path.exists('public/index.html'):
    shutil.copy('public/index.html', 'index.html')
    shutil.copy('public/admin.html', 'admin.html')
    shutil.copy('public/status.html', 'status.html')
    print("File berhasil disalin ke root.")
else:
    print("Folder public tidak ditemukan.")
