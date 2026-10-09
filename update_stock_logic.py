import re

# 1. Update index.html supaya kalau stock di database kosong/belum ada, tidak otomatis menimpa jadi 15 secara kaku, tapi mengikuti database.
with open('public/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Perbarui bagian loadCloudData untuk penanganan stok yang lebih fleksibel
old_stock_logic = '''                if (!stockErr && stockData && stockData.value !== undefined) {
                    currentStock = parseInt(stockData.value);
                    if (isNaN(currentStock)) currentStock = 15;
                } else {
                    currentStock = 15;
                }
                document.getElementById('liveStockBadge').innerText = `Sisa ${currentStock} Pcs Ready`;'''

new_stock_logic = '''                if (!stockErr && stockData && stockData.value !== undefined) {
                    currentStock = parseInt(stockData.value);
                    if (isNaN(currentStock)) currentStock = 0;
                } else {
                    currentStock = 15;
                }
                document.getElementById('liveStockBadge').innerText = `Sisa ${currentStock.toLocaleString('id-ID')} Pcs Ready`;'''

if old_stock_logic in content:
    content = content.replace(old_stock_logic, new_stock_logic)
    with open('public/index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("index.html stock logic updated successfully!")
else:
    print("Warning: index.html stock logic pattern not exact, checking alternative...")

