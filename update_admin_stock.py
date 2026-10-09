import os

admin_file = 'public/admin.html'
if os.path.exists(admin_file):
    with open(admin_file, 'r', encoding='utf-8') as f:
        admin_content = f.read()
    
    # Pastikan fungsi update stok di admin mendukung angka bebas/ribuan
    print("Admin file exists, verifying stock update handler...")
else:
    print("Admin file not found directly in public/, checking...")
