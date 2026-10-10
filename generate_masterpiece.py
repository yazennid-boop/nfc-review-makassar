# 1. index.html - Pelanggan (Tanpa Admin, Animasi Loading, Slogan Kuat, Shimmer, Status Toko Otomatis/Manual)
index_code = '''<!DOCTYPE html>
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
            0% { border-color: rgba(66, 133, 244, 0.4); box-shadow: 0 0 15px rgba(66, 133, 244, 0.1); }
            33% { border-color: rgba(234, 67, 53, 0.6); box-shadow: 0 0 25px rgba(234, 67, 53, 0.2); }
            66% { border-color: rgba(251, 188, 5, 0.6); box-shadow: 0 0 25px rgba(251, 188, 5, 0.2); }
            100% { border-color: rgba(52, 168, 83, 0.4); box-shadow: 0 0 15px rgba(52, 168, 83, 0.1); }
        }
        .shimmer-card { animation: borderShimmer 6s infinite ease-in-out; }

        @keyframes starGlow {
            0%, 100% { transform: scale(1); filter: drop-shadow(0 0 5px rgba(251, 188, 5, 0.5)); }
            50% { transform: scale(1.15); filter: drop-shadow(0 0 18px rgba(251, 188, 5, 0.95)); }
        }
        .star-glow { animation: starGlow 2.5s ease-in-out infinite; }

        @keyframes btnSweep {
            0% { transform: translateX(-100%); }
            100% { transform: translateX(100%); }
        }
        .shimmer-btn { position: relative; overflow: hidden; }
        .shimmer-btn::after {
            content: '';
            position: absolute;
            top: 0; left: -100%;
            width: 100%; height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.25), transparent);
            animation: btnSweep 3s infinite;
        }

        .glass-card {
            background: rgba(15, 23, 42, 0.96);
            backdrop-filter: blur(25px);
            border: 1px solid rgba(255, 255, 255, 0.12);
            box-shadow: 0 30px 60px -15px rgba(0, 0, 0, 0.85);
        }

        /* Loading Screen Overlay */
        #loadingScreen {
            position: fixed; inset: 0; background: #020617; z-index: 9999;
            display: flex; flex-direction: column; align-items: center; justify-content: center;
            transition: opacity 0.5s ease, visibility 0.5s ease;
        }
        .spinner {
            width: 50px; height: 50px; border: 4px solid rgba(66, 133, 244, 0.2);
            border-top: 4px solid #4285F4; border-radius: 50%;
            animation: spin 1s linear infinite;
        }
        @keyframes spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }
    </style>
</head>
<body class="bg-slate-950 text-slate-100 min-h-screen flex flex-col items-center justify-between p-3 md:p-6 selection:bg-blue-500 selection:text-white">

    <!-- Loading Overlay Premium -->
    <div id="loadingScreen">
        <div class="spinner mb-4"></div>
        <p class="text-xs font-mono text-blue-400 tracking-widest uppercase animate-pulse">Memuat Sistem NFC Makassar...</p>
    </div>

    <!-- Header Nav (Hanya Pusat Bantuan & TikTok Resmi, Tanpa Admin) -->
    <div class="w-full max-w-xl flex justify-between items-center mb-2 relative z-20">
        <a href="https://wa.me/6289504749648?text=Halo%20Admin,%20saya%20ingin%20berkonsultasi%20mengenai%20pemesanan%20kartu%20NFC%20Google%20Review." target="_blank" class="px-3.5 py-2 bg-slate-900/90 hover:bg-slate-800 text-blue-400 border border-blue-500/30 rounded-2xl text-[11px] font-bold transition flex items-center gap-2 shadow-lg">
            <i class="fa-solid fa-headset text-emerald-400"></i> <span>Pusat Bantuan & Konsultasi</span>
        </a>
        <a href="https://tiktok.com/@id.card_aff" target="_blank" class="px-3.5 py-2 bg-slate-900/90 hover:bg-slate-800 text-pink-400 border border-pink-500/30 rounded-2xl text-[11px] font-bold transition flex items-center gap-2 shadow-lg">
            <i class="fa-brands fa-tiktok"></i> <span>@id.card_aff</span>
        </a>
    </div>

    <!-- Main Container -->
    <main class="max-w-xl w-full glass-card rounded-3xl overflow-hidden space-y-6 relative z-10 my-2">
        <div class="h-2.5 google-bar"></div>

        <div class="p-6 md:p-8 space-y-6 pt-4">
            <!-- Banner & Info Stok -->
            <div class="text-center space-y-4">
                <div class="inline-flex items-center gap-2 px-3.5 py-1 rounded-full bg-blue-500/10 border border-blue-500/30 text-blue-400 text-[11px] font-bold uppercase tracking-wider shadow-inner">
                    <i class="fa-solid fa-location-dot text-rose-500"></i> Khusus Layanan Kilat Area Kota Makassar
                </div>

                <!-- Gambar Produk Utama -->
                <div class="relative w-full h-56 md:h-64 bg-slate-900 rounded-2xl border-2 shimmer-card overflow-hidden shadow-2xl flex items-center justify-center group">
                    <img src="nfc-card.jpg" alt="Kartu NFC Google Review" class="w-full h-full object-cover group-hover:scale-105 transition duration-700">
                    <div class="absolute inset-0 bg-gradient-to-t from-slate-950 via-slate-950/20 to-transparent flex items-end p-4">
                        <div class="w-full flex justify-between items-end">
                            <span class="px-2.5 py-1 bg-emerald-500/20 text-emerald-400 border border-emerald-500/30 rounded-lg text-[10px] font-bold">Teknologi Tap-In NFC & QR</span>
                            <span id="liveStockBadge" class="text-[10px] bg-blue-600/90 text-white px-3 py-1 rounded-md font-mono font-bold shadow-lg">Stok Ready: 15 Pcs</span>
                        </div>
                    </div>
                </div>

                <!-- Banner Toko (Otomatis/Manual) -->
                <div id="storeStatusBanner" class="hidden p-3.5 rounded-2xl text-xs font-semibold border text-center"></div>

                <!-- Slogan Memukau & Copywriting Marketing -->
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
                    <p class="text-xs md:text-sm text-slate-300 leading-relaxed px-1">
                        Tingkatkan reputasi digital, bangun kepercayaan pelanggan secara instan, dan dorong algoritma Local SEO bisnis Anda di Kota Makassar ke level tertinggi tanpa hambatan teknis.
                    </p>
                </div>
            </div>

            <!-- Form Pemesanan -->
            <div id="orderFormSection" class="space-y-4">
                <div class="bg-slate-950/90 p-4 rounded-2xl border border-slate-800 space-y-3 shadow-inner">
                    <label class="block text-xs font-bold text-slate-300 uppercase tracking-wide">Pilih Paket & Kuantitas Kartu NFC</label>
                    <div class="grid grid-cols-3 gap-2">
                        <button type="button" onclick="setPkg(1)" id="pkg1" class="pkg-btn p-3 rounded-xl border border-blue-500 bg-blue-500/15 text-center transition cursor-pointer hover:border-blue-400 shadow">
                            <span class="block text-xs font-bold text-white">1 Pcs</span>
                            <span class="text-[10px] text-blue-400 font-semibold">Rp 100rb</span>
                        </button>
                        <button type="button" onclick="setPkg(3)" id="pkg3" class="pkg-btn p-3 rounded-xl border border-slate-800 bg-slate-900 text-center transition cursor-pointer hover:border-slate-700">
                            <span class="block text-xs font-bold text-white">3 Pcs</span>
                            <span class="text-[10px] text-slate-400 font-semibold">Rp 300rb</span>
                        </button>
                        <button type="button" onclick="setPkg(5)" id="pkg5" class="pkg-btn p-3 rounded-xl border border-slate-800 bg-slate-900 text-center transition cursor-pointer hover:border-slate-700">
                            <span class="block text-xs font-bold text-white">5 Pcs</span>
                            <span class="text-[10px] text-slate-400 font-semibold">Rp 500rb</span>
                        </button>
                    </div>

                    <div class="flex justify-between items-center bg-slate-900 p-3 rounded-xl border border-slate-800 text-xs">
                        <span class="font-bold text-slate-300 uppercase">Jumlah Kustom (Pcs):</span>
                        <div class="flex items-center gap-2">
                            <button type="button" onclick="adjustQty(-1)" class="w-8 h-8 bg-slate-800 hover:bg-slate-700 text-white font-bold rounded-lg transition cursor-pointer">-</button>
                            <input type="number" id="customQty" value="1" min="1" max="100" oninput="calcTotal()" class="w-16 text-center py-1.5 bg-slate-950 border border-slate-700 rounded-lg text-white font-mono font-bold text-xs">
                            <button type="button" onclick="adjustQty(1)" class="w-8 h-8 bg-slate-800 hover:bg-slate-700 text-white font-bold rounded-lg transition cursor-pointer">+</button>
                        </div>
                    </div>
                </div>

                <div class="bg-slate-950/90 p-4 rounded-2xl border border-slate-800 space-y-3 text-xs">
                    <div>
                        <label class="block text-slate-400 mb-1 font-medium">Nama Lengkap Pemesan</label>
                        <input type="text" id="name" required placeholder="Masukkan nama lengkap" class="w-full px-3.5 py-2.5 bg-slate-900 border border-slate-800 rounded-xl text-white focus:outline-none focus:border-blue-500">
                    </div>
                    <div>
                        <label class="block text-slate-400 mb-1 font-medium">Nomor WhatsApp Aktif</label>
                        <input type="tel" id="whatsapp" required placeholder="Contoh: 081234567890" class="w-full px-3.5 py-2.5 bg-slate-900 border border-slate-800 rounded-xl text-white focus:outline-none focus:border-blue-500">
                    </div>
                    <div>
                        <label class="block text-slate-400 mb-1 font-medium">Nama Resmi Usaha / Toko</label>
                        <input type="text" id="businessName" required placeholder="Contoh: Cafe Kopi Makassar" class="w-full px-3.5 py-2.5 bg-slate-900 border border-slate-800 rounded-xl text-white focus:outline-none focus:border-blue-500">
                    </div>
                    <div>
                        <label class="block text-slate-400 mb-1 font-medium">Tautan Profil Google Maps Usaha</label>
                        <input type="url" id="mapsLink" required placeholder="Tempel tautan Google Maps tempat usaha" class="w-full px-3.5 py-2.5 bg-slate-900 border border-slate-800 rounded-xl text-white font-mono text-[11px] focus:outline-none focus:border-blue-500">
                    </div>
                    <div>
                        <label class="block text-slate-400 mb-1 font-medium">Tautan Titik Pengantaran (Sharelok Kurir)</label>
                        <input type="url" id="sharelokLink" required placeholder="Tempel tautan sharelok koordinat kurir" class="w-full px-3.5 py-2.5 bg-slate-900 border border-slate-800 rounded-xl text-white font-mono text-[11px] focus:outline-none focus:border-blue-500">
                    </div>
                    <div>
                        <label class="block text-slate-400 mb-1 font-medium">Patokan Alamat / Catatan Kurir</label>
                        <textarea id="addressDetail" rows="2" placeholder="Warna cat bangunan, dekat patokan tertentu..." class="w-full px-3.5 py-2 bg-slate-900 border border-slate-800 rounded-xl text-white focus:outline-none focus:border-blue-500"></textarea>
                    </div>
                    <div>
                        <label class="block text-slate-400 mb-1 font-medium">Estimasi Jarak Pengantaran dalam Kota Makassar (KM)</label>
                        <input type="number" id="distance" value="3" min="1" max="30" oninput="calcTotal()" class="w-full px-3.5 py-2.5 bg-slate-900 border border-slate-800 rounded-xl text-white focus:outline-none focus:border-blue-500">
                        <span class="text-[10px] text-slate-400 mt-1 block">*Tarif Kurir: ≤5km = Rp 5rb | 6-12km = Rp 10rb | >12km = Rp 15rb</span>
                    </div>
                </div>

                <div class="bg-slate-950/90 p-4 rounded-2xl border border-slate-800 space-y-2 text-xs font-medium">
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

                <button type="button" id="proceedBtn" onclick="goToPayment()" class="w-full py-4 bg-gradient-to-r from-blue-600 via-indigo-600 to-blue-600 hover:from-blue-500 hover:to-indigo-500 text-white font-bold rounded-xl text-xs transition shadow-lg shadow-blue-500/25 cursor-pointer uppercase tracking-wider shimmer-btn">
                    Lanjut ke Pembayaran QRIS
                </button>
            </div>

            <!-- Step 2: QRIS Payment -->
            <div id="paymentSection" class="hidden space-y-4 text-center">
                <div class="bg-slate-950/90 p-5 rounded-2xl border border-slate-800 space-y-3">
                    <h2 class="text-sm font-bold text-white">Selesaikan Pembayaran QRIS</h2>
                    <p class="text-xs text-slate-400">Pindai kode QRIS di bawah menggunakan aplikasi mobile banking atau e-wallet apa pun.</p>
                    <div class="bg-white p-3.5 rounded-2xl inline-block shadow-2xl">
                        <img src="qris.jpg" alt="QRIS Resmi" class="w-48 h-48 mx-auto object-contain rounded-lg">
                    </div>
                    <p class="text-xs text-amber-400 font-bold">Total Transfer: <span id="qrisTotal" class="text-white text-sm">Rp 105.000</span></p>
                </div>
                <div class="bg-slate-950/90 p-4 rounded-2xl border border-slate-800 text-left text-xs space-y-2">
                    <label class="block font-bold text-slate-300 uppercase">Unggah Bukti Transfer Resmi</label>
                    <input type="file" id="proofFile" accept="image/*" class="w-full text-xs text-slate-400 file:mr-3 file:py-2.5 file:px-4 file:rounded-xl file:border-0 file:text-xs file:font-semibold file:bg-blue-600 file:text-white cursor-pointer">
                </div>
                <div class="flex gap-2">
                    <button type="button" onclick="backToForm()" class="w-1/3 py-3.5 bg-slate-800 hover:bg-slate-700 text-white font-bold rounded-xl text-xs cursor-pointer">Kembali</button>
                    <button type="button" onclick="submitOrder()" class="w-2/3 py-3.5 bg-emerald-600 hover:bg-emerald-500 text-white font-bold rounded-xl text-xs shadow-lg font-bold cursor-pointer shimmer-btn">Konfirmasi & Kirim Pesanan</button>
                </div>
            </div>

            <!-- Step 3: Success -->
            <div id="successSection" class="hidden bg-slate-950/90 p-6 rounded-2xl border border-slate-800 text-center space-y-4">
                <div class="w-14 h-14 mx-auto rounded-full bg-emerald-500/20 text-emerald-400 flex items-center justify-center text-2xl border border-emerald-500/30 shadow-lg">
                    <i class="fa-solid fa-check"></i>
                </div>
                <h2 class="text-lg font-bold text-white">Pesanan Berhasil Disimpan!</h2>
                <p class="text-xs text-slate-300">ID Pesanan Anda: <code id="resultId" class="text-blue-400 font-mono font-bold"></code></p>
                <p class="text-[11px] text-slate-400">Silakan kirimkan detail pesanan ke WhatsApp admin agar kurir segera memproses pengantaran.</p>
                <a id="waConfirmBtn" href="#" target="_blank" class="block w-full py-3.5 bg-emerald-600 hover:bg-emerald-500 text-white font-bold rounded-xl text-xs transition shadow-lg shimmer-btn">
                    <i class="fa-brands fa-whatsapp text-sm"></i> Kirim Konfirmasi ke WhatsApp Admin
                </a>
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
                let loadEl = document.getElementById('loadingScreen');
                loadEl.style.opacity = '0';
                setTimeout(() => loadEl.style.display = 'none', 500);
            }, 600);

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

        function setPkg(qty) {
            currentQty = qty;
            document.getElementById('customQty').value = qty;
            document.querySelectorAll('.pkg-btn').forEach(b => {
                b.className = "pkg-btn p-3 rounded-xl border border-slate-800 bg-slate-900 text-center transition cursor-pointer hover:border-slate-700";
            });
            let active = document.getElementById(`pkg${qty}`);
            if (active) {
                active.className = "pkg-btn p-3 rounded-xl border border-blue-500 bg-blue-500/15 text-center transition cursor-pointer hover:border-blue-400 shadow";
            }
            calcTotal();
        }

        function adjustQty(val) {
            currentQty += val;
            if (currentQty < 1) currentQty = 1;
            if (currentQty > 100) currentQty = 100;
            document.getElementById('customQty').value = currentQty;
            document.querySelectorAll('.pkg-btn').forEach(b => {
                b.className = "pkg-btn p-3 rounded-xl border border-slate-800 bg-slate-900 text-center transition cursor-pointer hover:border-slate-700";
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
            let name = document.getElementById('name').value.trim();
            let wa = document.getElementById('whatsapp').value.trim();
            let biz = document.getElementById('businessName').value.trim();
            let maps = document.getElementById('mapsLink').value.trim();
            let sharelok = document.getElementById('sharelokLink').value.trim();

            if (!name || !wa || !biz || !maps || !sharelok) {
                alert('Mohon lengkapi seluruh formulir data usaha dan pengantaran.');
                return;
            }

            document.getElementById('orderFormSection').classList.add('hidden');
            document.getElementById('paymentSection').classList.remove('hidden');
        }

        function backToForm() {
            document.getElementById('paymentSection').classList.add('hidden');
            document.getElementById('orderFormSection').classList.remove('hidden');
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
                name: document.getElementById('name').value,
                whatsapp: document.getElementById('whatsapp').value,
                businessName: document.getElementById('businessName').value,
                mapsLink: document.getElementById('mapsLink').value,
                sharelokLink: document.getElementById('sharelokLink').value,
                addressDetail: document.getElementById('addressDetail').value,
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
                `*ID Pesanan:* ${orderId}\\n` +
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

with open('public/index.html', 'w', encoding='utf-8') as f:
    f.write(index_code)

# 2. admin.html - Panel Admin Profesional dengan Tombol Izin Notifikasi & Suara Cash Register
admin_code = '''<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>Admin Dashboard - NFC Google Review Makassar</title>
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
        .glass-card {
            background: rgba(15, 23, 42, 0.96);
            backdrop-filter: blur(25px);
            border: 1px solid rgba(255, 255, 255, 0.12);
            box-shadow: 0 30px 60px -15px rgba(0, 0, 0, 0.85);
        }
    </style>
</head>
<body class="bg-slate-950 text-slate-100 min-h-screen flex flex-col items-center justify-between p-3 md:p-6 selection:bg-blue-500 selection:text-white">

    <!-- Login Screen -->
    <div id="loginScreen" class="max-w-md w-full glass-card rounded-3xl overflow-hidden shadow-2xl relative z-10 my-auto">
        <div class="h-2.5 google-bar"></div>
        <div class="p-6 md:p-8 space-y-6">
            <div class="text-center space-y-2">
                <div class="w-12 h-12 mx-auto rounded-full bg-blue-500/10 text-blue-400 flex items-center justify-center border border-blue-500/30 text-xl">
                    <i class="fa-solid fa-shield-halved"></i>
                </div>
                <h1 class="text-xl font-bold text-white">Otorisasi Panel Admin</h1>
                <p class="text-xs text-slate-400">Area aman khusus pengelola sistem.</p>
            </div>
            
            <div class="space-y-4 text-xs">
                <div>
                    <label class="block text-slate-400 mb-1 font-medium">Password Admin</label>
                    <div class="relative">
                        <input type="password" id="adminPassword" placeholder="Masukkan password..." class="w-full px-3.5 py-3 pr-10 bg-slate-900 border border-slate-800 rounded-xl text-white focus:outline-none focus:border-blue-500 font-mono">
                        <button type="button" onclick="togglePass()" class="absolute right-3 top-1/2 -translate-y-1/2 text-slate-400 hover:text-white cursor-pointer p-1">
                            <i id="eyeIcon" class="fa-solid fa-eye"></i>
                        </button>
                    </div>
                </div>
                <div id="loginError" class="text-red-400 text-[11px] font-semibold hidden"></div>
                <button type="button" onclick="handleLogin()" class="w-full py-3.5 bg-blue-600 hover:bg-blue-500 text-white font-bold rounded-xl transition shadow-lg shadow-blue-500/25 cursor-pointer uppercase tracking-wider">
                    Masuk ke Dashboard
                </button>
            </div>
        </div>
    </div>

    <!-- Dashboard Panel -->
    <div id="dashboardPanel" class="hidden max-w-5xl w-full glass-card rounded-3xl overflow-hidden shadow-2xl relative z-10 my-4">
        <div class="h-2.5 google-bar"></div>
        
        <div class="p-6 md:p-8 space-y-6">
            <div class="flex flex-col md:flex-row justify-between items-start md:items-center gap-4 border-b border-slate-800 pb-5">
                <div>
                    <span class="px-2.5 py-1 bg-emerald-500/20 text-emerald-400 border border-emerald-500/30 rounded-lg text-[10px] font-bold">Secure Admin Session Active</span>
                    <h1 class="text-xl md:text-2xl font-extrabold text-white mt-1">Manajemen Pesanan & Operasional Toko</h1>
                </div>
                <div class="flex flex-wrap items-center gap-2">
                    <button type="button" onclick="requestNotificationPermission()" class="px-3.5 py-2 bg-blue-500/20 hover:bg-blue-500/30 text-blue-400 border border-blue-500/30 rounded-xl text-xs font-bold transition flex items-center gap-1.5 cursor-pointer">
                        <i class="fa-solid fa-bell"></i> <span>Aktifkan Notifikasi Pesanan</span>
                    </button>
                    <button type="button" onclick="clearAllOrders()" class="px-3.5 py-2 bg-red-500/10 hover:bg-red-500/20 text-red-400 border border-red-500/30 rounded-xl text-xs font-bold transition flex items-center gap-1.5 cursor-pointer">
                        <i class="fa-solid fa-trash-can"></i> <span>Hapus Semua Riwayat</span>
                    </button>
                    <button type="button" onclick="handleLogout()" class="px-3.5 py-2 bg-slate-800 hover:bg-slate-700 text-slate-300 rounded-xl text-xs font-bold transition flex items-center gap-1.5 cursor-pointer">
                        <i class="fa-solid fa-right-from-bracket"></i> <span>Keluar</span>
                    </button>
                </div>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs">
                <div class="bg-slate-900/90 p-4 rounded-2xl border border-slate-800 space-y-2">
                    <label class="block font-bold text-slate-300 uppercase">Setup Sisa Stok Perangkat NFC</label>
                    <div class="flex gap-2">
                        <input type="number" id="stockInput" class="w-full px-3 py-2 bg-slate-950 border border-slate-800 rounded-xl text-white font-mono font-bold">
                        <button type="button" onclick="updateStock()" class="px-4 py-2 bg-blue-600 hover:bg-blue-500 text-white font-bold rounded-xl transition cursor-pointer shrink-0 shadow">Simpan</button>
                    </div>
                </div>
                <div class="bg-slate-900/90 p-4 rounded-2xl border border-slate-800 flex flex-col justify-between">
                    <span class="font-bold text-slate-300 uppercase">Kontrol Status Toko (Buka / Tutup Manual)</span>
                    <div class="flex items-center justify-between mt-2">
                        <span id="storeStatusLabel" class="font-bold text-emerald-400">Buka (Normal)</span>
                        <button type="button" id="toggleStoreBtn" onclick="toggleStoreManual()" class="px-4 py-2 bg-slate-800 hover:bg-slate-700 text-white font-bold rounded-xl transition cursor-pointer shadow">Tutup Toko</button>
                    </div>
                </div>
            </div>

            <div class="space-y-3">
                <div class="flex justify-between items-center">
                    <h2 class="text-sm font-bold text-white uppercase tracking-wide flex items-center gap-2">
                        <i class="fa-solid fa-list-check text-blue-400"></i> Daftar Pesanan Masuk Pelanggan
                    </h2>
                    <span id="orderCountBadge" class="px-2.5 py-0.5 rounded-full bg-blue-500/20 text-blue-400 text-xs font-mono font-bold">0 Pesanan</span>
                </div>

                <div class="overflow-x-auto rounded-2xl border border-slate-800 bg-slate-900/50">
                    <table class="w-full text-left text-xs">
                        <thead class="bg-slate-900 text-slate-400 uppercase font-bold border-b border-slate-800">
                            <tr>
                                <th class="p-3.5">ID & Waktu Pesan</th>
                                <th class="p-3.5">Pemesan & Toko</th>
                                <th class="p-3.5">Patokan & Kurir</th>
                                <th class="p-3.5">Detail Paket</th>
                                <th class="p-3.5">Status</th>
                                <th class="p-3.5 text-center">Aksi Konfirmasi</th>
                            </tr>
                        </thead>
                        <tbody id="ordersTableBody" class="divide-y divide-slate-800 text-slate-300">
                            <tr>
                                <td colspan="6" class="p-6 text-center text-slate-500">Belum ada pesanan masuk.</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    </div>

    <footer class="w-full py-4 text-center text-[11px] text-slate-500 relative z-10">
        &copy; 2026 NFC Google Review Makassar. All Rights Reserved.
    </footer>

    <script>
        const CORRECT_PASSWORD = "Yasir Sigma";
        let lastOrderCount = 0;

        function togglePass() {
            let p = document.getElementById('adminPassword');
            let icon = document.getElementById('eyeIcon');
            if (p.type === 'password') {
                p.type = 'text';
                icon.className = 'fa-solid fa-eye-slash';
            } else {
                p.type = 'password';
                icon.className = 'fa-solid fa-eye';
            }
        }

        function requestNotificationPermission() {
            if (!("Notification" in window)) {
                alert("Browser ini tidak mendukung sistem notifikasi desktop.");
                return;
            }
            Notification.requestPermission().then(permission => {
                if (permission === "granted") {
                    alert("Izin notifikasi berhasil diaktifkan! Anda akan menerima pemberitahuan saat ada pesanan masuk.");
                    new Notification("NFC Makassar", { body: "Sistem notifikasi pesanan aktif." });
                } else {
                    alert("Izin notifikasi ditolak.");
                }
            });
        }

        function playCashRegisterSound() {
            try {
                const ctx = new (window.AudioContext || window.webkitAudioContext)();
                const osc = ctx.createOscillator();
                const gain = ctx.createGain();
                osc.type = 'triangle';
                osc.frequency.setValueAtTime(1318.51, ctx.currentTime);
                gain.gain.setValueAtTime(0.4, ctx.currentTime);
                gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + 0.6);
                osc.connect(gain);
                gain.connect(ctx.destination);
                osc.start();
                osc.stop(ctx.currentTime + 0.6);
            } catch (e) {
                console.log("Audio dibatasi.");
            }
        }

        function handleLogin() {
            let pass = document.getElementById('adminPassword').value.trim();
            let err = document.getElementById('loginError');
            if (pass === CORRECT_PASSWORD) {
                localStorage.setItem('nfc_admin_token', 'token_' + Date.now());
                showDashboard();
            } else {
                err.classList.remove('hidden');
                err.innerText = "Password salah! Gunakan: Yasir Sigma";
            }
        }

        function handleLogout() {
            localStorage.removeItem('nfc_admin_token');
            document.getElementById('dashboardPanel').classList.add('hidden');
            document.getElementById('loginScreen').classList.remove('hidden');
            document.getElementById('adminPassword').value = '';
        }

        function showDashboard() {
            document.getElementById('loginScreen').classList.add('hidden');
            document.getElementById('dashboardPanel').classList.remove('hidden');
            loadAdminData();
            setInterval(pollNewOrders, 4000);
        }

        function loadAdminData() {
            let stock = localStorage.getItem('nfc_stock');
            if (stock === null) {
                stock = '15';
                localStorage.setItem('nfc_stock', stock);
            }
            document.getElementById('stockInput').value = stock;

            let manualClose = localStorage.getItem('nfc_manual_close') === 'true';
            let label = document.getElementById('storeStatusLabel');
            let btn = document.getElementById('toggleStoreBtn');

            if (manualClose) {
                label.innerText = "Tutup (Sibuk / Manual)";
                label.className = "font-bold text-red-400";
                btn.innerText = "Buka Toko";
            } else {
                label.innerText = "Buka (Normal)";
                label.className = "font-bold text-emerald-400";
                btn.innerText = "Tutup Toko";
            }
            renderOrders();
        }

        function updateStock() {
            let val = document.getElementById('stockInput').value;
            localStorage.setItem('nfc_stock', val);
            alert('Stok perangkat berhasil diperbarui menjadi ' + val + ' Pcs.');
            loadAdminData();
        }

        function toggleStoreManual() {
            let manualClose = localStorage.getItem('nfc_manual_close') === 'true';
            localStorage.setItem('nfc_manual_close', !manualClose);
            loadAdminData();
        }

        function renderOrders() {
            let orders = JSON.parse(localStorage.getItem('nfc_orders')) || [];
            let tbody = document.getElementById('ordersTableBody');
            document.getElementById('orderCountBadge').innerText = orders.length + " Pesanan";

            if (orders.length === 0) {
                tbody.innerHTML = `<tr><td colspan="6" class="p-6 text-center text-slate-500">Belum ada pesanan masuk.</td></tr>`;
                lastOrderCount = 0;
                return;
            }

            lastOrderCount = orders.length;
            tbody.innerHTML = '';
            orders.slice().reverse().forEach((order) => {
                let idx = orders.findIndex(o => o.orderId === order.orderId);
                let tr = document.createElement('tr');
                let status = order.processStatus || 'Menunggu Konfirmasi';
                tr.className = "hover:bg-slate-800/40 transition";
                tr.innerHTML = `
                    <td class="p-3.5 font-mono">
                        <span class="text-white font-bold">${order.orderId}</span><br>
                        <span class="text-[10px] text-amber-400"><i class="fa-regular fa-clock"></i> ${order.date}</span>
                    </td>
                    <td class="p-3.5">
                        <span class="text-white font-bold">${order.name}</span> (${order.whatsapp})<br>
                        <span class="text-blue-400 font-medium">${order.businessName}</span><br>
                        <a href="${order.mapsLink}" target="_blank" class="text-[10px] text-slate-400 hover:underline">🔗 Maps Usaha</a>
                    </td>
                    <td class="p-3.5">
                        <p class="text-slate-200 font-medium bg-slate-950 p-2 rounded-lg border border-slate-800 text-[11px] mb-1">
                            📍 ${order.addressDetail || 'Tidak ada catatan.'}
                        </p>
                        <a href="${order.sharelokLink}" target="_blank" class="text-[10px] text-blue-400 font-bold hover:underline">📍 Titik Sharelok</a>
                    </td>
                    <td class="p-3.5">
                        ${order.qty} Pcs<br>
                        <span class="text-emerald-400 font-bold">Rp ${order.total.toLocaleString('id-ID')}</span>
                    </td>
                    <td class="p-3.5">
                        <span class="px-2 py-1 rounded-md text-[10px] font-bold ${status === 'Selesai & Dikirim' ? 'bg-emerald-500/20 text-emerald-400' : 'bg-blue-500/20 text-blue-400'}">${status}</span>
                    </td>
                    <td class="p-3.5 text-center space-x-1 whitespace-nowrap">
                        <button type="button" onclick="updateStatus(${idx}, 'Sedang Dikirim Kurir')" class="px-2 py-1.5 bg-blue-600 hover:bg-blue-500 text-white rounded-lg text-[10px] font-bold transition cursor-pointer">Kirim</button>
                        <button type="button" onclick="updateStatus(${idx}, 'Selesai & Dikirim')" class="px-2 py-1.5 bg-emerald-600 hover:bg-emerald-500 text-white rounded-lg text-[10px] font-bold transition cursor-pointer">Selesai</button>
                        <button type="button" onclick="deleteOrder(${idx})" class="px-2 py-1.5 bg-red-600/20 hover:bg-red-600 text-red-400 hover:text-white border border-red-500/30 rounded-lg text-[10px] transition cursor-pointer"><i class="fa-solid fa-trash"></i></button>
                    </td>
                `;
                tbody.appendChild(tr);
            });
        }

        function pollNewOrders() {
            let orders = JSON.parse(localStorage.getItem('nfc_orders')) || [];
            if (orders.length > lastOrderCount) {
                playCashRegisterSound();
                if (Notification.permission === "granted") {
                    new Notification("Pesanan Baru Masuk! 🎉", { body: `Ada pesanan baru dengan ID ${orders[orders.length-1].orderId}` });
                }
                renderOrders();
            }
        }

        function updateStatus(idx, status) {
            let orders = JSON.parse(localStorage.getItem('nfc_orders')) || [];
            if (orders[idx]) {
                orders[idx].processStatus = status;
                localStorage.setItem('nfc_orders', JSON.stringify(orders));
                renderOrders();
            }
        }

        function deleteOrder(idx) {
            if (confirm('Hapus riwayat pesanan ini?')) {
                let orders = JSON.parse(localStorage.getItem('nfc_orders')) || [];
                orders.splice(idx, 1);
                localStorage.setItem('nfc_orders', JSON.stringify(orders));
                renderOrders();
            }
        }

        function clearAllOrders() {
            if (confirm('Yakin ingin menghapus SELURUH riwayat pesanan?')) {
                localStorage.removeItem('nfc_orders');
                renderOrders();
                alert('Riwayat pesanan dibersihkan.');
            }
        }

        window.onload = function() {
            let token = localStorage.getItem('nfc_admin_token');
            if (token && token.startsWith('token_')) {
                showDashboard();
            } else {
                handleLogout();
            }
        }
    </script>
</body>
</html>
'''

with open('public/admin.html', 'w', encoding='utf-8') as f:
    f.write(admin_code)

# 3. status.html - Pelacakan Status Pesanan
status_code = '''<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>Status Pesanan - NFC Google Review Makassar</title>
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
        .glass-card {
            background: rgba(15, 23, 42, 0.96);
            backdrop-filter: blur(25px);
            border: 1px solid rgba(255, 255, 255, 0.12);
            box-shadow: 0 30px 60px -15px rgba(0, 0, 0, 0.85);
        }
    </style>
</head>
<body class="bg-slate-950 text-slate-100 min-h-screen flex flex-col items-center justify-between p-3 md:p-6 selection:bg-blue-500 selection:text-white">

    <div class="w-full max-w-lg flex justify-between items-center mb-2 relative z-20">
        <a href="index.html" class="px-3 py-2 bg-slate-900/90 hover:bg-slate-800 text-blue-400 border border-blue-500/30 rounded-2xl text-[11px] font-bold transition flex items-center gap-2 shadow-lg">
            <i class="fa-solid fa-arrow-left"></i> <span>Kembali ke Beranda</span>
        </a>
        <a href="https://wa.me/6289504749648?text=Halo%20Admin,%20saya%20ingin%20menanyakan%20status%20pesanan%20saya." target="_blank" class="px-3 py-2 bg-slate-900/90 hover:bg-slate-800 text-emerald-400 border border-emerald-500/30 rounded-2xl text-[11px] font-bold transition flex items-center gap-1.5 shadow-lg">
            <i class="fa-brands fa-whatsapp text-sm"></i> <span>Hubungi Admin</span>
        </a>
    </div>

    <main class="max-w-lg w-full glass-card rounded-3xl overflow-hidden space-y-6 relative z-10 my-4">
        <div class="h-2.5 google-bar"></div>

        <div class="p-6 md:p-8 space-y-6 pt-2">
            <div class="text-center space-y-2">
                <div class="w-12 h-12 mx-auto rounded-full bg-blue-500/10 text-blue-400 flex items-center justify-center border border-blue-500/30 text-xl">
                    <i class="fa-solid fa-truck-fast"></i>
                </div>
                <h1 class="text-xl font-bold text-white">Pelacakan Status Pesanan</h1>
                <p class="text-xs text-slate-400">Masukkan ID Pesanan atau lihat pesanan terakhir Anda.</p>
            </div>

            <div class="space-y-3 text-xs">
                <div>
                    <label class="block text-slate-400 mb-1 font-medium">ID Pesanan (Contoh: NFC-123456)</label>
                    <div class="flex gap-2">
                        <input type="text" id="searchIdInput" placeholder="Masukkan ID Pesanan..." class="w-full px-3.5 py-3 bg-slate-900 border border-slate-800 rounded-xl text-white uppercase font-mono focus:outline-none focus:border-blue-500">
                        <button type="button" onclick="searchOrder()" class="px-5 py-3 bg-blue-600 hover:bg-blue-500 text-white font-bold rounded-xl transition cursor-pointer shrink-0">Cari</button>
                    </div>
                </div>
            </div>

            <div id="resultContainer" class="hidden space-y-4 pt-4 border-t border-slate-800"></div>
        </div>
    </main>

    <footer class="w-full py-4 text-center text-[11px] text-slate-500 relative z-10">
        &copy; 2026 NFC Google Review Makassar. All Rights Reserved.
    </footer>

    <script>
        window.onload = function() {
            let lastId = localStorage.getItem('last_order_id');
            if (lastId) {
                document.getElementById('searchIdInput').value = lastId;
                searchOrder();
            }
        }

        function searchOrder() {
            let id = document.getElementById('searchIdInput').value.trim().toUpperCase();
            let container = document.getElementById('resultContainer');
            container.classList.remove('hidden');

            if (!id) {
                container.innerHTML = `<p class="text-red-400 text-center text-xs">Masukkan ID Pesanan yang valid.</p>`;
                return;
            }

            let orders = JSON.parse(localStorage.getItem('nfc_orders')) || [];
            let found = orders.find(o => o.orderId.toUpperCase() === id);

            if (!found) {
                container.innerHTML = `<p class="text-amber-400 text-center text-xs">Pesanan dengan ID <b>${id}</b> tidak ditemukan.</p>`;
                return;
            }

            let status = found.processStatus || 'Menunggu Konfirmasi';
            let badgeClass = "bg-amber-500/20 text-amber-400 border-amber-500/30";
            let icon = "fa-clock";
            let desc = "Pesanan sedang menunggu verifikasi pembayaran oleh admin.";

            if (status === 'Sedang Dikirim Kurir') {
                badgeClass = "bg-blue-500/20 text-blue-400 border-blue-500/30";
                icon = "fa-truck-fast";
                desc = "Kurir sedang dalam perjalanan mengantar pesanan ke lokasi usaha Anda di Makassar.";
            } else if (status === 'Selesai & Dikirim') {
                badgeClass = "bg-emerald-500/20 text-emerald-400 border-emerald-500/30";
                icon = "fa-circle-check";
                desc = "Pesanan telah selesai diantar dan diterima dengan baik. Terima kasih!";
            }

            container.innerHTML = `
                <div class="bg-slate-900/90 p-4 rounded-2xl border border-slate-800 space-y-3 text-xs">
                    <div class="flex justify-between items-center border-b border-slate-800 pb-2.5">
                        <span class="font-mono font-bold text-white text-sm">${found.orderId}</span>
                        <span class="px-2.5 py-1 rounded-lg font-bold border text-[10px] ${badgeClass} flex items-center gap-1.5">
                            <i class="fa-solid ${icon}"></i> ${status}
                        </span>
                    </div>

                    <div class="space-y-1.5 text-slate-300">
                        <p><b>Nama Pemesan:</b> ${found.name} (${found.whatsapp})</p>
                        <p><b>Nama Usaha:</b> <span class="text-blue-400 font-semibold">${found.businessName}</span></p>
                        <p><b>Patokan Alamat:</b> ${found.addressDetail || '-'}</p>
                        <p><b>Jumlah Paket:</b> ${found.qty} Pcs</p>
                        <p><b>Total Pembayaran:</b> <span class="text-emerald-400 font-bold">Rp ${found.total.toLocaleString('id-ID')}</span></p>
                        <p><b>Waktu Pesan:</b> <span class="text-slate-400 font-mono">${found.date}</span></p>
                    </div>

                    <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 text-[11px] text-slate-300 flex items-start gap-2">
                        <i class="fa-solid fa-circle-info text-blue-400 mt-0.5"></i>
                        <span>${desc}</span>
                    </div>

                    <div class="pt-2">
                        <a href="https://wa.me/6289504749648?text=Halo%20Admin,%20saya%20ingin%20menanyakan%20status%20pengiriman%20untuk%20ID%20Pesanan%20${found.orderId}" target="_blank" class="block w-full py-3 bg-emerald-600 hover:bg-emerald-500 text-white font-bold text-center rounded-xl transition shadow-lg">
                            <i class="fa-brands fa-whatsapp"></i> Konfirmasi via WhatsApp Admin
                        </a>
                    </div>
                </div>
            `;
        }
    </script>
</body>
</html>
'''

with open('public/status.html', 'w', encoding='utf-8') as f:
    f.write(status_code)

print("Masterpiece files successfully generated!")
