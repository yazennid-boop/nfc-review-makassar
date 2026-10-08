const express = require('express');
const path = require('path');
const fs = require('fs');
const multer = require('multer');
const rateLimit = require('express-rate-limit');
const cors = require('cors');

const app = express();
const PORT = 3000;

app.set('trust proxy', 1);

app.use(cors());
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

const orderLimiter = rateLimit({
  windowMs: 15 * 60 * 1000,
  max: 30,
  message: { success: false, message: 'Terlalu banyak permintaan, coba lagi nanti.' }
});

const uploadDir = path.join(__dirname, 'public', 'uploads');
if (!fs.existsSync(uploadDir)) {
  fs.mkdirSync(uploadDir, { recursive: true });
}

const storage = multer.diskStorage({
  destination: (req, file, cb) => cb(null, uploadDir),
  filename: (req, file, cb) => {
    const uniqueSuffix = Date.now() + '-' + Math.round(Math.random() * 1E9);
    cb(null, 'transfer-' + uniqueSuffix + path.extname(file.originalname));
  }
});

const upload = multer({
  storage: storage,
  limits: { fileSize: 5 * 1024 * 1024 }
});

let storeConfig = {
  isOpen: true,
  stock: 3,
  pricePerPcs: 100000,
  promoCode: 'MAKASSARNFC',
  discountAmount: 20000,
  adminWA: '6289504749648'
};

let orders = [];

app.use(express.static(path.join(__dirname, 'public')));

app.get('/api/store-status', (req, res) => {
  res.json({
    isOpen: storeConfig.isOpen && storeConfig.stock > 0,
    stock: storeConfig.stock,
    pricePerPcs: storeConfig.pricePerPcs,
    adminWA: storeConfig.adminWA,
    orders: orders
  });
});

app.post('/api/check-promo', (req, res) => {
  const { code } = req.body;
  if (code && code.trim().toUpperCase() === storeConfig.promoCode) {
    return res.json({ 
      valid: true, 
      discount: storeConfig.discountAmount,
      message: 'Kode Promo Berhasil Dipakai! Diskon Rp 20.000 / Pcs' 
    });
  }
  res.json({ valid: false, message: 'Kode promo tidak valid atau salah!' });
});

app.post('/api/track-order', (req, res) => {
  const { query } = req.body;
  const found = orders.find(o => o.orderId.toLowerCase() === query.trim().toLowerCase() || o.whatsapp === query.trim());
  if (found) {
    res.json({ success: true, order: found });
  } else {
    res.json({ success: false, message: 'Pesanan tidak ditemukan. Periksa kembali ID Order atau No WA Anda.' });
  }
});

app.post('/api/update-stock', (req, res) => {
  const { newStock } = req.body;
  const parsedStock = parseInt(newStock);
  if (!isNaN(parsedStock) && parsedStock >= 0) {
    storeConfig.stock = parsedStock;
    return res.json({ success: true, message: `Stok berhasil diubah menjadi ${parsedStock} Pcs!`, stock: storeConfig.stock });
  }
  res.status(400).json({ success: false, message: 'Angka stok tidak valid!' });
});

app.post('/api/reset-orders', (req, res) => {
  orders = [];
  res.json({ success: true, message: 'Semua daftar pesanan berhasil di-reset!' });
});

app.post('/api/order', orderLimiter, upload.single('paymentProof'), (req, res) => {
  try {
    if (storeConfig.stock <= 0 || !storeConfig.isOpen) {
      return res.status(400).json({ success: false, message: 'Stok habis atau toko sedang tutup!' });
    }

    const { 
      name, whatsapp, businessName, businessProfileLink, 
      deliverySharelock, addressDetail, bookingDate, packageType, appliedPromo, distanceKm 
    } = req.body;

    const qty = parseInt(packageType) || 1;
    if (qty > storeConfig.stock) {
      return res.status(400).json({ success: false, message: `Sisa stok hanya ${storeConfig.stock} Pcs!` });
    }

    let isPromoValid = appliedPromo && appliedPromo.trim().toUpperCase() === storeConfig.promoCode;
    let discountPerPcs = isPromoValid ? storeConfig.discountAmount : 0;
    let itemTotal = (storeConfig.pricePerPcs - discountPerPcs) * qty;

    let km = parseFloat(distanceKm) || 1;
    let shippingFee = 5000; 
    if (km > 5 && km <= 12) {
      shippingFee = 10000; 
    } else if (km > 12) {
      shippingFee = 15000; 
    }

    let totalPrice = itemTotal + shippingFee;
    const orderId = 'NFC-' + Math.floor(100000 + Math.random() * 900000);

    const newOrder = {
      orderId,
      name,
      whatsapp,
      businessName,
      businessProfileLink,
      deliverySharelock,
      addressDetail,
      bookingDate,
      packageType: `Paket ${qty} (${qty} Pcs)`,
      qty,
      distanceKm: km,
      shippingFee,
      totalPrice,
      appliedPromo: isPromoValid ? storeConfig.promoCode : 'Tidak Ada',
      paymentProof: req.file ? `/uploads/${req.file.filename}` : null,
      paymentStatus: 'SUDAH TERBAYAR',
      processStatus: 'Diproses & Menunggu Aktivasi',
      createdAt: new Date()
    };

    orders.push(newOrder);
    storeConfig.stock = Math.max(0, storeConfig.stock - qty);

    res.json({ success: true, orderId, message: 'Pesanan berhasil dibuat!' });
  } catch (error) {
    res.status(500).json({ success: false, message: error.message });
  }
});

app.get('/', (req, res) => res.sendFile(path.join(__dirname, 'public', 'index.html')));
app.get('/admin', (req, res) => res.sendFile(path.join(__dirname, 'public', 'admin.html')));
app.get('/status', (req, res) => res.sendFile(path.join(__dirname, 'public', 'status.html')));

app.listen(PORT, '0.0.0.0', () => {
  console.log(`Server NFC System Aktif di http://0.0.0.0:${PORT}`);
});
