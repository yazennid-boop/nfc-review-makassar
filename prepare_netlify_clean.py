import os
import shutil

# Memastikan folder public bersih dan berisi file utama yang diperlukan
os.makedirs('public', exist_ok=True)
if os.path.exists('index.html'):
    shutil.copy('index.html', 'public/index.html')

print("File bersih untuk Netlify siap di folder public/.")
