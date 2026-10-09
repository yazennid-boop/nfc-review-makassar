import re

with open('public/index.html', 'r', encoding='utf-8') as f:
    code = f.read()

# Ganti semua fallback 15 yang ada di file index.html menjadi 3
code = code.replace("currentStock = 15;", "currentStock = 3;")
code = code.replace("currentStock = parseInt(stockData.value);", "currentStock = parseInt(stockData.value) || 3;")

with open('public/index.html', 'w', encoding='utf-8') as f:
    f.write(code)

print("Fallback stock 15 successfully replaced!")
