📡 CCTV Explorer by Paan
https://img.shields.io/badge/Python-3.6+-blue.svg
https://img.shields.io/badge/License-MIT-green.svg

🎯 Tentang Proyek
CCTV Explorer by Paan adalah aplikasi Python yang memudahkan Anda mengakses CCTV live dari berbagai kota di Indonesia melalui satu platform terintegrasi. Dengan antarmuka yang user-friendly dan navigasi yang intuitif, Anda dapat dengan cepat menemukan dan membuka stream CCTV dari kota-kota besar hingga daerah di seluruh Indonesia.

✨ Fitur Utama
🏙️ Koleksi Lengkap - Akses CCTV dari 50+ kota di Indonesia

🎨 Antarmuka Menarik - Tampilan colorful dengan animasi dan efek visual

⚡ Akses Cepat - Buka langsung CCTV di browser dengan satu klik

🔍 Pencarian Mudah - Daftar kota terorganisir dalam format kolom

🎯 User-Friendly - Navigasi sederhana dengan prompt yang jelas

🌈 Pengalaman Visual - Efek mengetik, loading animation, dan warna terminal

🚀 Cara Menggunakan
Jalankan aplikasi:

bash
python cctv_explorer.py
Pilih opsi:

Masukkan 1 untuk memilih kota

Masukkan 2 untuk keluar

Masukkan nama kota yang ingin dilihat CCTV-nya

Konfirmasi untuk membuka link di browser

📋 Daftar Kota Tersedia
Aplikasi ini mendukung 50+ kota termasuk:

Jakarta, Surabaya, Bandung, Yogyakarta, Bali

Medan, Makassar, Semarang, Denpasar, Malang

Kota-kota besar lainnya di seluruh Indonesia

🛠️ Teknologi
Python 3.6+

Modul webbrowser untuk akses browser

Modul time untuk animasi

Modul os untuk manipulasi terminal

ANSI Color Codes untuk tampilan berwarna

📁 Struktur Kode
text
cctv_explorer.py
├── cctv_urls (Dictionary 50+ kota)
├── print_header() - Tampilan header
├── typewriter_effect() - Efek mengetik
├── animate_loading() - Animasi loading
├── show_kota_available() - Daftar kota
└── get_cctv_link() - Fungsi utama
⚡ Quick Start
python
# Clone dan jalankan
python cctv_explorer.py
🎨 Preview
text
==========================================================
🛰️           CCTV EXPLORER BY PAAN           🛰️
==========================================================

Selamat datang di CCTV Explorer by Paan!
Aplikasi untuk mengakses CCTV live dari berbagai kota di Indonesia

Daftar Kota yang Tersedia:
--------------------------------------------------
📍 Jakarta    📍 Surabaya     📍 Bandung     
📍 Yogyakarta 📍 Bali         📍 Medan       
... [dan seterusnya]
💡 Catatan
Pastikan koneksi internet tersedia

Beberapa CCTV mungkin memerlukan waktu loading

Aplikasi optimal di terminal yang support ANSI colors

👨‍💻 Developer
Dibuat dengan ❤️ oleh Paan

"Exploring Indonesia, one CCTV at a time" 🌏
