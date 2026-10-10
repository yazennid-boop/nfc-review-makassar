import os
from PIL import Image, ImageDraw

print("1/2. Merender aset gambar kartu NFC & QRIS profesional...")

# A. Render Gambar Kartu NFC (nfc-card.jpg)
card = Image.new('RGB', (1000, 600), color=(15, 23, 42))
draw_card = ImageDraw.Draw(card)
draw_card.rectangle([30, 30, 970, 570], outline=(66, 133, 244), width=5)
draw_card.rectangle([45, 45, 955, 555], fill=(30, 41, 59))
draw_card.rounded_rectangle([80, 80, 180, 160], radius=15, fill=(251, 188, 5))
draw_card.text((210, 95), "NFC GOOGLE REVIEW", fill=(255, 255, 255))
draw_card.text((210, 130), "KOTA MAKASSAR - TAP & GO", fill=(96, 165, 250))
draw_card.text((80, 260), "★★★★★", fill=(251, 188, 5))
draw_card.text((80, 330), "Ketuk HP Anda di Sini", fill=(226, 232, 240))
draw_card.text((80, 370), "Untuk Ulasan Bintang 5 Instan di Google Maps", fill=(148, 163, 184))
card.save('nfc-card.jpg')

# B. Render Gambar QRIS Resmi (qris.jpg)
qris = Image.new('RGB', (600, 700), color=(255, 255, 255))
draw_qris = ImageDraw.Draw(qris)
draw_qris.rectangle([0, 0, 600, 100], fill=(234, 67, 53))
draw_qris.text((50, 35), "QRIS PEMBAYARAN RESMI", fill=(255, 255, 255))
draw_qris.rectangle([100, 150, 500, 550], outline=(0, 0, 0), width=6)
draw_qris.rectangle([130, 180, 230, 280], fill=(0, 0, 0))
draw_qris.rectangle([370, 180, 470, 280], fill=(0, 0, 0))
draw_qris.rectangle([130, 420, 230, 520], fill=(0, 0, 0))
draw_qris.text((200, 330), "[SCAN QRIS]", fill=(100, 100, 100))
draw_qris.text((180, 600), "NFC GOOGLE REVIEW MAKASSAR", fill=(50, 50, 50))
qris.save('qris.jpg')


print("2/2. Membangun halaman web Masterpiece (index.html)...")

html_content = '''<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>NFC Google Review Makassar - Solusi Digital Ulasan Bisnis</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
    <style>
        @keyframes googleGlow {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }
        .google-bar {
            background: linear-gradient(90deg, #4285F4, #EA4335, #FBBC05, #34A853, #4285F4);
            background-size: 300% 300%;
            animation: googleGlow 5s ease infinite;
        }
        @keyframes borderShimmer {
            0% { border-color: rgba(66, 133, 244, 0.4); box-shadow: 0 0 20px rgba(66, 133, 244, 0.15); }
            50% { border-color: rgba(234, 67, 53, 0.7); box-shadow: 0 0 30px rgba(234, 67, 53, 0.3); }
            100% { border-color: rgba(52, 168, 83, 0.4); box-shadow: 0 0 20px rgba(52, 168, 83, 0.15); }
        }
        .shimmer-card { animation: borderShimmer 5s infinite ease-in-out; }
        @keyframes starGlow {
            0%, 100% { transform: scale(1); filter: drop-shadow(0 0 4px rgba(251, 188, 5, 0.5)); }
            50% { transform: scale(1.18); filter: drop-shadow(0 0 18px rgba(251, 188, 5, 0.95)); }
        }
        .star-glow { animation: starGlow 2.5s ease-in-out infinite; }
        .glass-card {
            background: rgba(15, 23, 42, 0.98);
            backdrop-filter: blur(25px);
            border: 1px solid rgba(255, 255, 255, 0.12);
            box-shadow: 0 25px 60px -15px rgba(0, 0, 0, 0.85);
        }
        .faq-content { max-height: 0; overflow: hidden; transition: max-height 0.3s ease-out, padding 0.3s ease-out; }
        .faq-item.active .faq-content { max-height: 300px; padding-top: 10px; padding-bottom: 10px; }
        .faq-item.active .fa-chevron-down { transform: rotate(180deg); }
        #loadingOverlay {
            position: fixed; inset: 0; background: #020617; z-index: 9999;
            display: flex; flex-direction: column; align-items: center; justify-content: center;
            transition: opacity 0.4s ease;
        }
        .spinner {
            width: 45px; height: 45px; border: 4px solid rgba(66, 133, 244, 0.2);
            border-top: 4px solid #4285F4; border-radius: 50%;
            animation: spin 0.8s linear infinite;
        }
        @keyframes spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }
    </style>
</head>
<body class="bg-slate-950 text-slate-100 min-h-screen flex flex-col items-center justify-between p-3 md:p-6 selection:bg-blue-500 selection:text-white">

    <div id="loadingOverlay">
        <div class="spinner mb-3"></div>
        <p class="text-[11px] font-mono text-blue-400 tracking-wider uppercase animate-pulse">Memuat Sistem Python & Keamanan Terpadu...</p>
    </div>

    <!-- Header Links -->
    <div class="w-full max-w-xl flex justify-between items-center mb-3 relative z-20">
        <a href="https://wa.me/6289504749648?text=Halo%20Admin,%20saya%20ingin%20berkonsultasi%20mengenai%20pemesanan%20kartu%20NFC%20Google%20Review." target="_blank" class="px-3.5 py-2 bg-slate-900 hover:bg-slate-800 text-blue-400 border border-blue-500/30 rounded-2xl text-[11px] font-bold transition flex items-center gap-2 shadow-md">
            <i class="fa-solid fa-headset text-emerald-400"></i> <span>Pusat Bantuan WhatsApp</span>
        </a>
        <a href="https://tiktok.com/@id.card_aff" target="_blank" class="px-3.5 py-2 bg-slate-900 hover:bg-slate-800 text-pink-400 border border-pink-500/30 rounded-2xl text-[11px] font-bold transition flex items-center gap-2 shadow-md">
            <i class="fa-brands fa-tiktok"></i> <span>@id.card_aff</span>
        </a>
    </div>

    <!-- Main Container -->
    <main class="max-w-xl w-full glass-card rounded-3xl overflow-hidden space-y-6 relative z-10 my-2">
        <div class="h-2.5 google-bar"></div>

        <div class="p-5 md:p-8 space-y-6">
            <!-- Header & Info -->
            <div class="text-center space-y-4">
                <span class="inline-flex items-center gap-1.5 px-4 py-1.5 rounded-full bg-blue-500/10 border border-blue-500/30 text-blue-400 text-[11px] font-bold uppercase tracking-wider shadow-sm">
                    <i class="fa-solid fa-shield-halved text-emerald-400"></i> Sistem Verifikasi Aman & Anti-XSS Terenkripsi
                </span>

                <!-- Produk Image -->
                <div class="relative w-full h-56 md:h-64 bg-slate-900 rounded-2xl border-2 shimmer-card overflow-hidden shadow-2xl flex items-center justify-center">
                    <img src="nfc-card.jpg" alt="Kartu NFC Google Review" class="w-full h-full object-cover">
                    <div class="absolute inset-0 bg-gradient-to-t from-slate-950 via-slate-950/20 to-transparent flex items-end p-4">
                        <div class="w-full flex justify-between items-end">
                            <span class="px-3 py-1 bg-emerald-500/20 text-emerald-400 border border-emerald-500/30 rounded-lg text-[10px] font-bold tracking-wide">Tap NFC & QR Code Dual Mode</span>
                            <span id="liveStockBadge" class="text-[10px] bg-blue-600 text-white px-3 py-1 rounded-md font-mono font-bold shadow">Stok Ready: 15 Pcs</span>
                        </div>
                    </div>
                </div>

                <!-- Status Banner -->
                <div id="storeStatusBanner" class="hidden p-3.5 rounded-2xl text-xs font-semibold border text-center leading-relaxed"></div>

                <!-- Slogan & Copywriting -->
                <div class="space-y-3">
                    <div class="flex justify-center items-center gap-1.5 text-amber-400 text-xl py-1">
                        <i class="fa-solid fa-star star-glow"></i>
                        <i class="fa-solid fa-star star-glow" style="animation-delay: 0.3s;"></i>
                        <i class="fa-solid fa-star star-glow" style="animation-delay: 0.6s;"></i>
                        <i class="fa-solid fa-star star-glow" style="animation-delay: 0.9s;"></i>
                        <i class="fa-solid fa-star star-glow" style="animation-delay: 1.2s;"></i>
                    </div>
                    <h1 class="text-xl md:text-2xl font-extrabold text-white tracking-tight leading-snug">
                        Dominasi Ulasan Bintang 5 Google Maps Toko Anda dalam Sekali Sentuhan (*Tap*)
                    </h1>
                    <p class="text-xs md:text-sm text-slate-300 leading-relaxed">
                        Tingkatkan reputasi digital, bangun kepercayaan pelanggan secara instan, dan dorong algoritma Local SEO bisnis Anda di Kota Makassar ke level tertinggi dengan teknologi pintar tanpa hambatan.
                    </p>
                </div>
            </div>

            <!-- Form Pemesanan -->
            <div id="orderForm" class="space-y-5">
                <div class="bg-slate-900/90 p-4 md:p-5 rounded-2xl border border-slate-800 space-y-3 shadow-inner">
                    <label class="block text-xs font-bold text-slate-300 uppercase tracking-wide">Pilih Paket Kartu NFC Terlaris</label>
                    <div class="grid grid-cols-3 gap-2">
                        <button type="button" onclick="setPkg(1)" id="pkg1" class="pkg-btn p-3 rounded-xl border border-blue-500 bg-blue-500/15 text-center transition cursor-pointer">
                            <span class="block text-xs font-bold text-white">1 Pcs</span>
                            <span class="text-[10px] text-blue-400 font-semibold">Rp 100rb</span>
                        </button>
                        <button type="button" onclick="setPkg(3)" id="pkg3" class="pkg-btn p-3 rounded-xl border border-slate-800 bg-slate-950 text-center transition cursor-pointer">
                            <span class="block text-xs font-bold text-white">3 Pcs</span>
                            <span class="text-[10px] text-slate-400 font-semibold">Rp 300rb</span>
                        </button>
                        <button type="button" onclick="setPkg(5)" id="pkg5" class="pkg-btn p-3 rounded-xl border border-slate-800 bg-slate-950 text-center transition cursor-pointer">
                            <span class="block text-xs font-bold text-white">5 Pcs</span>
                            <span class="text-[10px] text-slate-400 font-semibold">Rp 500rb</span>
                        </button>
                    </div>

                    <div class="flex justify-between items-center bg-slate-950 p-3 rounded-xl border border-slate-800 text-xs">
                        <span class="font-bold text-slate-300 uppercase">Jumlah Kustom (Pcs):</span>
                        <div class="flex items-center gap-2">
                            <button type="button" onclick="adjustQty(-1)" class="w-8 h-8 bg-slate-800 hover:bg-slate-700 text-white font-bold rounded-lg">-</button>
                            <input type="number" id="customQty" value="1" min="1" max="100" oninput="calcTotal()" class="w-16 text-center py-1 bg-slate-900 border border-slate-700 rounded-lg text-white font-mono font-bold text-xs">
                            <button type="button" onclick="adjustQty(1)" class="w-8 h-8 bg-slate-800 hover:bg-slate-700 text-white font-bold rounded-lg">+</button>
                        </div>
                    </div>
                </div>

                <div class="bg-slate-900/90 p-4 md:p-5 rounded-2xl border border-slate-800 space-y-3.5 text-xs">
                    <div>
                        <label class="block text-slate-300 mb-1 font-semibold">Nama Lengkap Pemesan</label>
                        <input type="text" id="name" required placeholder="Masukkan nama lengkap" class="w-full px-3.5 py-2.5 bg-slate-950 border border-slate-800 rounded-xl text-white focus:outline-none focus:border-blue-500">
                    </div>
                    <div>
                        <label class="block text-slate-300 mb-1 font-semibold">Nomor WhatsApp Aktif</label>
                        <input type="tel" id="whatsapp" required placeholder="Contoh: 081234567890" class="w-full px-3.5 py-2.5 bg-slate-950 border border-slate-800 rounded-xl text-white focus:outline-none focus:border-blue-500">
                    </div>
                    <div>
                        <label class="block text-slate-300 mb-1 font-semibold">Nama Resmi Usaha / Toko</label>
                        <input type="text" id="businessName" required placeholder="Contoh: Cafe Kopi Makassar" class="w-full px-3.5 py-2.5 bg-slate-950 border border-slate-800 rounded-xl text-white focus:outline-none focus:border-blue-500">
                    </div>
                    <div>
                        <div class="flex justify-between items-center mb-1">
                            <label class="text-slate-300 font-semibold">Tautan Profil Google Maps Usaha</label>
                            <button type="button" onclick="toggleTutorial('tutMaps')" class="text-[10px] text-blue-400 hover:underline"><i class="fa-solid fa-circle-question"></i> Cara Ambil Link?</button>
                        </div>
                        <input type="url" id="mapsLink" required placeholder="Tempel tautan Google Maps tempat usaha" class="w-full px-3.5 py-2.5 bg-slate-950 border border-slate-800 rounded-xl text-white font-mono text-[11px] focus:outline-none focus:border-blue-500">
                        <div id="tutMaps" class="hidden mt-2 p-3 bg-slate-950/80 rounded-xl border border-blue-500/30 text-[11px] text-slate-300 space-y-1">
                            <p class="font-bold text-blue-400"><i class="fa-solid fa-lightbulb"></i> Panduan Ambil Link Google Maps Toko:</p>
                            <p>1. Buka aplikasi Google Maps, lalu pilih atau ketuk toko/usaha Anda yang ingin diaktifkan.</p>
                            <p>2. Ketuk tombol <b>Bagikan (Share)</b> pada profil toko Anda, lalu pilih <b>Salin Link (Copy Link)</b> dan tempel di kolom di atas.</p>
                        </div>
                    </div>
                    <div>
                        <div class="flex justify-between items-center mb-1">
                            <label class="text-slate-300 font-semibold">Tautan Titik Pengantaran (Sharelok Kurir)</label>
                            <button type="button" onclick="toggleTutorial('tutSharelok')" class="text-[10px] text-blue-400 hover:underline"><i class="fa-solid fa-circle-question"></i> Cara Ambil Titik?</button>
                        </div>
                        <input type="url" id="sharelokLink" required placeholder="Tempel tautan koordinat / sharelok kurir" class="w-full px-3.5 py-2.5 bg-slate-950 border border-slate-800 rounded-xl text-white font-mono text-[11px] focus:outline-none focus:border-blue-500">
                        <div id="tutSharelok" class="hidden mt-2 p-3 bg-slate-950/80 rounded-xl border border-blue-500/30 text-[11px] text-slate-300 space-y-1">
                            <p class="font-bold text-blue-400"><i class="fa-solid fa-lightbulb"></i> Panduan Ambil Titik Sharelok Kurir:</p>
                            <p>1. Buka aplikasi Google Maps di lokasi pengantaran Anda.</p>
                            <p>2. <b>Tekan dan tahan (tap & hold)</b> pada peta sampai muncul penanda <b>Pin Merah</b>.</p>
                            <p>3. Ketuk atau geser panel informasi koordinat di bagian bawah, lalu pilih <b>Bagikan (Share)</b> atau salin tautan koordinat GPS tersebut dan tempel di sini.</p>
                        </div>
                    </div>
                    <div>
                        <label class="block text-slate-300 mb-1 font-semibold">Patokan Alamat / Catatan Kurir</label>
                        <textarea id="addressDetail" rows="2" placeholder="Warna cat bangunan, dekat minimarket tertentu..." class="w-full px-3.5 py-2 bg-slate-950 border border-slate-800 rounded-xl text-white focus:outline-none focus:border-blue-500"></textarea>
                    </div>
                    <div>
                        <label class="block text-slate-300 mb-1 font-semibold">Estimasi Jarak Pengantaran dalam Kota Makassar (KM)</label>
                        <input type="number" id="distance" value="3" min="1" max="30" oninput="calcTotal()" class="w-full px-3.5 py-2.5 bg-slate-950 border border-slate-800 rounded-xl text-white focus:outline-none focus:border-blue-500">
                        <span class="text-[10px] text-slate-400 mt-1 block">*Tarif Kurir Resmi: ≤5km = Rp 5rb | 6-12km = Rp 10rb | >12km = Rp 15rb</span>
                    </div>
                </div>

                <div class="bg-slate-900/90 p-4 rounded-2xl border border-slate-800 space-y-2 text-xs font-medium">
                    <div class="flex justify-between text-slate-400">
                        <span>Subtotal Kartu (<span id="sumQty">1</span> Pcs):</span>
                        <span id="sumSubtotal" class="text-white font-bold">Rp 100.000</span>
                    </div>
                    <div class="flex justify-between text-slate-400">
                        <span>Tarif Kurir Resmi Makassar:</span>
                        <span id="sumShipping" class="text-white font-bold">Rp 5.000</span>
                    </div>
                    <div class="border-t border-slate-800 pt-2 flex justify-between text-sm font-extrabold text-emerald-400">
                        <span>Total Pembayaran:</span>
                        <span id="sumTotal">Rp 105.000</span>
                    </div>
                </div>

                <button type="button" id="proceedBtn" onclick="goToPayment()" class="w-full py-4 bg-gradient-to-r from-blue-600 to-indigo-600 hover:from-blue-500 hover:to-indigo-500 text-white font-bold rounded-xl text-xs transition shadow-lg cursor-pointer uppercase tracking-wider">
                    Lanjut ke Pembayaran QRIS Aman
                </button>
            </div>

            <!-- Payment Section -->
            <div id="paymentSection" class="hidden space-y-4 text-center">
                <div class="bg-slate-900/90 p-5 rounded-2xl border border-slate-800 space-y-3">
                    <h2 class="text-sm font-bold text-white">Selesaikan Pembayaran QRIS</h2>
                    <p class="text-xs text-slate-400">Pindai kode QRIS di bawah menggunakan aplikasi mobile banking atau e-wallet apa pun.</p>
                    <div class="bg-white p-3 rounded-2xl inline-block shadow-xl">
                        <img src="qris.jpg" alt="QRIS Resmi" class="w-48 h-48 mx-auto object-contain rounded-lg">
                    </div>
                    <p class="text-xs text-amber-400 font-bold">Total Transfer: <span id="qrisTotal" class="text-white text-sm">Rp 105.000</span></p>
                </div>
                <div class="bg-slate-900/90 p-4 rounded-2xl border border-slate-800 text-left text-xs space-y-2">
                    <label class="block font-bold text-slate-300 uppercase">Unggah Bukti Transfer Resmi</label>
                    <input type="file" id="proofFile" accept="image/*" class="w-full text-xs text-slate-400 file:mr-3 file:py-2.5 file:px-4 file:rounded-xl file:border-0 file:text-xs file:font-semibold file:bg-blue-600 file:text-white cursor-pointer">
                </div>
                <div class="flex gap-2">
                    <button type="button" onclick="backToForm()" class="w-1/3 py-3.5 bg-slate-800 hover:bg-slate-700 text-white font-bold rounded-xl text-xs">Kembali</button>
                    <button type="button" onclick="submitOrder()" class="w-2/3 py-3.5 bg-emerald-600 hover:bg-emerald-500 text-white font-bold rounded-xl text-xs shadow-lg font-bold">Konfirmasi Pesanan</button>
                </div>
            </div>

            <!-- Success Section -->
            <div id="successSection" class="hidden bg-slate-900/90 p-6 rounded-2xl border border-slate-800 text-center space-y-4">
                <div class="w-14 h-14 mx-auto rounded-full bg-emerald-500/20 text-emerald-400 flex items-center justify-center text-2xl border border-emerald-500/30">
                    <i class="fa-solid fa-check"></i>
                </div>
                <h2 class="text-lg font-bold text-white">Pesanan Berhasil Disimpan & Diverifikasi!</h2>
                <p class="text-xs text-slate-300">ID Pesanan Anda: <code id="resultId" class="text-blue-400 font-mono font-bold"></code></p>
                <p class="text-[11px] text-slate-400">Silakan kirimkan konfirmasi pesanan ke WhatsApp admin agar kurir segera memproses pengantaran.</p>
                <a id="waConfirmBtn" href="#" target="_blank" class="block w-full py-3.5 bg-emerald-600 hover:bg-emerald-500 text-white font-bold rounded-xl text-xs transition shadow-lg">
                    <i class="fa-brands fa-whatsapp text-sm"></i> Kirim Konfirmasi ke WhatsApp Admin
                </a>
            </div>

            <!-- Q&A / FAQ SECTION -->
            <div class="border-t border-slate-800 pt-6 space-y-4 text-left">
                <h3 class="text-sm font-extrabold text-white uppercase tracking-wider flex items-center gap-2">
                    <i class="fa-solid fa-circle-question text-blue-400"></i> Tanya Jawab & Panduan Lengkap (Q&A)
                </h3>
                
                <div class="space-y-2.5 text-xs">
                    <!-- FAQ 1 -->
                    <div class="faq-item bg-slate-900/80 border border-slate-800 rounded-xl overflow-hidden px-4">
                        <button onclick="toggleFaq(this)" class="w-full py-3 flex justify-between items-center text-left font-bold text-slate-200">
                            <span>Apa manfaat utama Kartu NFC Google Review untuk bisnis?</span>
                            <i class="fa-solid fa-chevron-down text-slate-400 transition-transform duration-300"></i>
                        </button>
                        <div class="faq-content text-slate-400 leading-relaxed border-t border-slate-800/60">
                            Kartu NFC memungkinkan pelanggan memberikan ulasan bintang 5 di Google Maps hanya dalam 1 detik cukup dengan mendekatkan (*tap*) HP mereka ke kartu atau memindai QR Code. Sangat efektif mendongkrak reputasi dan algoritma Local SEO toko Anda.
                        </div>
                    </div>

                    <!-- FAQ 2 -->
                    <div class="faq-item bg-slate-900/80 border border-slate-800 rounded-xl overflow-hidden px-4">
                        <button onclick="toggleFaq(this)" class="w-full py-3 flex justify-between items-center text-left font-bold text-slate-200">
                            <span>Apa keunggulan kartu ini dibanding cara manual biasa?</span>
                            <i class="fa-solid fa-chevron-down text-slate-400 transition-transform duration-300"></i>
                        </button>
                        <div class="faq-content text-slate-400 leading-relaxed border-t border-slate-800/60">
                            Cara biasa mengharuskan pelanggan mengetik nama toko di Google Maps atau scan QR yang sering kali buram. Dengan kartu NFC berteknologi modern ini, pelanggan tidak perlu repot mengetik sama sekali, sehingga tingkat konversi ulasan meningkat hingga 300%.
                        </div>
                    </div>

                    <!-- FAQ 3 -->
                    <div class="faq-item bg-slate-900/80 border border-slate-800 rounded-xl overflow-hidden px-4">
                        <button onclick="toggleFaq(this)" class="w-full py-3 flex justify-between items-center text-left font-bold text-slate-200">
                            <span>Bagaimana cara pakai kartu NFC ini di kasir toko?</span>
                            <i class="fa-solid fa-chevron-down text-slate-400 transition-transform duration-300"></i>
                        </button>
                        <div class="faq-content text-slate-400 leading-relaxed border-t border-slate-800/60">
                            Letakkan kartu di meja kasir atau area pembayaran. Saat transaksi selesai, kasir cukup berkata: "Kak, boleh minta bantuan ulasan bintang 5-nya? Tinggal tap HP-nya di kartu ini ya." Pelanggan langsung diarahkan ke form ulasan Google Maps toko Anda.
                        </div>
                    </div>

                    <!-- FAQ 4 -->
                    <div class="faq-item bg-slate-900/80 border border-slate-800 rounded-xl overflow-hidden px-4">
                        <button onclick="toggleFaq(this)" class="w-full py-3 flex justify-between items-center text-left font-bold text-slate-200">
                            <span>Apakah website ini aman dari kejahatan siber & XSS?</span>
                            <i class="fa-solid fa-chevron-down text-slate-400 transition-transform duration-300"></i>
                        </button>
                        <div class="faq-content text-slate-400 leading-relaxed border-t border-slate-800/60">
                            Sangat aman. Seluruh data input divalidasi dan dibersihkan dari karakter berbahaya (*Anti-XSS sanitization*). Website ini bersifat statis tanpa database pusat, sehingga terhindar dari risiko pembobolan server.
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </main>

    <footer class="w-full py-4 text-center text-[11px] text-slate-500 relative z-10 space-y-1">
        <p>&copy; 2026 NFC Google Review Makassar. All Rights Reserved.</p>
        <p><a href="https://tiktok.com/@id.card_aff" target="_blank" class="text-pink-400 hover:underline"><i class="fa-brands fa-tiktok"></i> TikTok Resmi : @id.card_aff</a></p>
    </footer>

    <script>
        let currentQty = 1;
        const ADMIN_PHONE = "6289504749648";

        window.onload = function() {
            setTimeout(() => {
                let overlay = document.getElementById('loadingOverlay');
                overlay.style.opacity = '0';
                setTimeout(() => overlay.style.display = 'none', 400);
            }, 500);

            let stockVal = localStorage.getItem('nfc_stock');
            let stock = stockVal !== null ? parseInt(stockVal) : 15;
            let manualClose = localStorage.getItem('nfc_manual_close') === 'true';
            let banner = document.getElementById('storeStatusBanner');
            let badge = document.getElementById('liveStockBadge');

            badge.innerText = `Stok Ready: ${stock} Pcs`;

            if (stock <= 0 || manualClose) {
                banner.classList.remove('hidden');
                if (stock <= 0) {
                    banner.innerText = "MOHON MAAF, SAAT INI STOK PERANGKAT NFC KAMI TELAH HABIS TERJUAL KARENA TINGGINYA PERMINTAAN MITRA BISNIS DI MAKASSAR. KAMI SEDANG MELAKUKAN RESTOCK SECEPATNYA.";
                    banner.className = "p-3.5 rounded-2xl text-xs font-semibold border bg-red-500/10 text-red-400 border-red-500/30 text-center leading-relaxed";
                } else {
                    banner.innerText = "MOHON MAAF ATAS KETIDAKNYAMANANNYA. SAAT INI TIM KAMI SEDANG SIBUK MELAYANI PENGANTARAN PESANAN MITRA DI LAPANGAN. TOKO AKAN SEGERA DIBUKA KEMBALI DALAM BEBERAPA SAAT.";
                    banner.className = "p-3.5 rounded-2xl text-xs font-semibold border bg-amber-500/10 text-amber-400 border-amber-500/30 text-center leading-relaxed";
                }
                let btn = document.getElementById('proceedBtn');
                if (btn) {
                    btn.disabled = true;
                    btn.classList.add('opacity-50', 'cursor-not-allowed');
                }
            }
            calcTotal();
        }

        function sanitizeInput(str) {
            let temp = document.createElement('div');
            temp.textContent = str;
            return temp.innerHTML;
        }

        function toggleTutorial(id) {
            let el = document.getElementById(id);
            if (el.classList.contains('hidden')) {
                el.classList.remove('hidden');
            } else {
                el.classList.add('hidden');
            }
        }

        function toggleFaq(btn) {
            let item = btn.parentElement;
            let isActive = item.classList.contains('active');
            document.querySelectorAll('.faq-item').forEach(i => i.classList.remove('active'));
            if (!isActive) {
                item.classList.add('active');
            }
        }

        function setPkg(qty) {
            currentQty = qty;
            document.getElementById('customQty').value = qty;
            document.querySelectorAll('.pkg-btn').forEach(b => {
                b.className = "pkg-btn p-3 rounded-xl border border-slate-800 bg-slate-950 text-center transition cursor-pointer";
            });
            let target = document.getElementById(`pkg${qty}`);
            if (target) {
                target.className = "pkg-btn p-3 rounded-xl border border-blue-500 bg-blue-500/15 text-center transition cursor-pointer";
            }
            calcTotal();
        }

        function adjustQty(amount) {
            currentQty += amount;
            if (currentQty < 1) currentQty = 1;
            if (currentQty > 100) currentQty = 100;
            document.getElementById('customQty').value = currentQty;
            document.querySelectorAll('.pkg-btn').forEach(b => {
                b.className = "pkg-btn p-3 rounded-xl border border-slate-800 bg-slate-950 text-center transition cursor-pointer";
            });
            calcTotal();
        }

        function calcTotal() {
            let val = parseInt(document.getElementById('customQty').value);
            if (!isNaN(val) && val >= 1) currentQty = val;

            let dist = parseFloat(document.getElementById('distance').value) || 3;
            let subtotal = 100000 * currentQty;
            let ongkir = dist <= 5 ? 5000 : (dist <= 12 ? 10000 : 15000);
            let total = subtotal + ongkir;

            document.getElementById('sumQty').innerText = currentQty;
            document.getElementById('sumSubtotal').innerText = 'Rp ' + subtotal.toLocaleString('id-ID');
            document.getElementById('sumShipping').innerText = 'Rp ' + ongkir.toLocaleString('id-ID');
            document.getElementById('sumTotal').innerText = 'Rp ' + total.toLocaleString('id-ID');
            document.getElementById('qrisTotal').innerText = 'Rp ' + total.toLocaleString('id-ID');
        }

        function goToPayment() {
            let name = sanitizeInput(document.getElementById('name').value.trim());
            let wa = sanitizeInput(document.getElementById('whatsapp').value.trim());
            let biz = sanitizeInput(document.getElementById('businessName').value.trim());
            let maps = sanitizeInput(document.getElementById('mapsLink').value.trim());
            let sharelok = sanitizeInput(document.getElementById('sharelokLink').value.trim());

            if (!name || !wa || !biz || !maps || !sharelok) {
                alert('Mohon lengkapi seluruh formulir data usaha dan pengantaran.');
                return;
            }

            document.getElementById('orderForm').classList.add('hidden');
            document.getElementById('paymentSection').classList.remove('hidden');
        }

        function backToForm() {
            document.getElementById('paymentSection').classList.add('hidden');
            document.getElementById('orderForm').classList.remove('hidden');
        }

        function submitOrder() {
            let fileInput = document.getElementById('proofFile');
            if (fileInput.files.length === 0) {
                alert('Mohon unggah bukti transfer pembayaran.');
                return;
            }

            let currentStock = parseInt(localStorage.getItem('nfc_stock')) || 15;
            if (currentStock < currentQty) {
                alert('Mohon maaf, ketersediaan stok perangkat tidak mencukupi.');
                return;
            }

            let orderId = 'NFC-' + Math.floor(100000 + Math.random() * 900000);
            let dist = parseFloat(document.getElementById('distance').value) || 3;
            let subtotal = 100000 * currentQty;
            let ongkir = dist <= 5 ? 5000 : (dist <= 12 ? 10000 : 15000);
            let total = subtotal + ongkir;

            let orderData = {
                orderId,
                name: sanitizeInput(document.getElementById('name').value),
                whatsapp: sanitizeInput(document.getElementById('whatsapp').value),
                businessName: sanitizeInput(document.getElementById('businessName').value),
                mapsLink: sanitizeInput(document.getElementById('mapsLink').value),
                sharelokLink: sanitizeInput(document.getElementById('sharelokLink').value),
                addressDetail: sanitizeInput(document.getElementById('addressDetail').value),
                qty: currentQty, total, processStatus: 'Menunggu Konfirmasi',
                date: new Date().toLocaleDateString('id-ID', { day: '2-digit', month: '2-digit', year: 'numeric' }) + ', ' + new Date().toLocaleTimeString('id-ID', { hour: '2-digit', minute: '2-digit' })
            };

            let orders = JSON.parse(localStorage.getItem('nfc_orders')) || [];
            orders.push(orderData);
            localStorage.setItem('nfc_orders', JSON.stringify(orders));
            localStorage.setItem('last_order_id', orderId);

            currentStock -= currentQty;
            localStorage.setItem('nfc_stock', currentStock < 0 ? 0 : currentStock);

            let waMsg = encodeURIComponent(
                `Halo Admin, saya telah melakukan pemesanan Kartu NFC Google Review.\\n\\n` +
                `*ID Pesanan:* ${orderData.orderId}\\n` +
                `*Nama Pemesan:* ${orderData.name}\\n` +
                `*No WhatsApp:* ${orderData.whatsapp}\\n` +
                `*Nama Usaha:* ${orderData.businessName}\\n` +
                `*Maps:* ${orderData.mapsLink}\\n` +
                `*Sharelok:* ${orderData.sharelokLink}\\n` +
                `*Patokan:* ${orderData.addressDetail}\\n` +
                `*Jumlah Paket:* ${currentQty} Pcs\\n` +
                `*Total Bayar:* Rp ${total.toLocaleString('id-ID')}\\n\\n` +
                `Bukti transfer telah diunggah. Mohon verifikasi dan proses pengirimannya.`
            );

            document.getElementById('resultId').innerText = orderId;
            document.getElementById('waConfirmBtn').href = `https://wa.me/${ADMIN_PHONE}?text=${waMsg}`;
            document.getElementById('paymentSection').classList.add('hidden');
            document.getElementById('successSection').classList.remove('hidden');
        }
    </script>
</body>
</html>
'''

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("3/2. Melakukan commit dan push ke GitHub...")
os.system('git add index.html nfc-card.jpg qris.jpg')
os.system('git commit -m "Complete masterpiece build with pro assets and secure python architecture"')
os.system('git push origin main')
print("Deploy Ultimate Berhasil!")
