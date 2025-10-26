import webbrowser
import time
import os
import sys

# Daftar kota dan URL CCTV yang relevan
cctv_urls = {
    "Jakarta": "https://atcs-jakarta.com/Maps",
    "Surabaya": "https://lewatmana.com/kota/surabaya/",
    "Bandung": "https://atcs.bandungbaratkab.go.id/",
    "Yogyakarta": "https://cctv.jogjakota.go.id/",
    "Bali": "https://balisatudata.baliprov.go.id/peta-cctv",
    "Medan": "https://atcsdishub.pemkomedan.go.id/",
    "Makassar": "https://tolmakassar.com/cctv",
    "Semarang": "https://pantausemar.semarangkota.go.id/",
    "Denpasar": "https://balisatudata.baliprov.go.id/peta-cctv",
    "Malang": "http://cctv.malangkota.go.id/",
    "Surakarta": "https://cctv-dishub.sukoharjokab.go.id/",
    "Palembang": "https://www.palembangport.co.id/cctv/",
    "Batam": "https://dishub.batam.go.id/cctv-lalu-lintas-kota-batam/",
    "Balikpapan": "http://tmckotabalikpapan.id/",
    "Samarinda": "https://diskominfo.samarindakota.go.id/media/cctv",
    "Tangerang": "https://live.tangerangkota.go.id/atcs/",
    "Depok": "http://cctv.depok.go.id:8083/",
    "Bogor": "https://bsw.kotabogor.go.id/cctv",
    "Cirebon": "https://atcs.cirebonkab.go.id/",
    "Pontianak": "https://jepin.pontianak.go.id/cctv",
    "Banjarmasin": "https://cctv.banjarmasinkota.go.id/",
    "Mataram": "https://cctv.badilag.net/display/satker/71f02bb5fb80808a88bd99f61134ced6",
    "Kupang": "https://pa-kupang.go.id/en/informasi-pengadilan/318-cctv-online.html",
    "Jambi": "https://cctv.badilag.net/display/satker/42a9bcb14747db700fa8928be77361e0",
    "Solo": "https://ccroom-dishub.surakarta.go.id/",
    "Palu": "https://cctv.pa-palu.go.id/",
    "Ambon": "https://cctv.badilag.net/display/satker/2a0471ee9d94e5fe5d9aec0e3bcbc570",
    "Ciputat": "https://lewatmana.com/cam/208/juanda-lebak-bulus/",
    "Sukabumi": "https://lewatmana.com/cari/?q=sukabumi",
    "Bekasi": "https://lewatmana.com/kota/bekasi/",
    "Tegal": "https://dishub.tegalkota.go.id/cctv",
    "Pekalongan": "https://dishub.pekalongankota.go.id/cctv",
    "Madiun": "https://dishub.madiunkota.go.id/cctv",
    "Kediri": "https://dishub.kedirikota.go.id/cctv",
    "Blitar": "https://dishub.blitarkota.go.id/cctv",
    "Probolinggo": "https://dishub.probolinggokota.go.id/cctv",
    "Pasuruan": "https://dishub.pasuruankota.go.id/cctv",
    "Mojokerto": "https://dishub.mojokertokota.go.id/cctv",
    "Magelang": "https://dishub.magelangkota.go.id/cctv",
    "Salatiga": "https://dishub.salatiga.go.id/cctv",
    "Cilacap": "https://dishub.cilacapkab.go.id/cctv",
    "Banyuwangi": "https://dishub.banyuwangikab.go.id/cctv",
    "Jember": "https://dishub.jemberkab.go.id/cctv",
    "Lumajang": "https://dishub.lumajangkab.go.id/cctv",
    "Bondowoso": "https://dishub.bondowosokab.go.id/cctv",
    "Situbondo": "https://dishub.situbondokab.go.id/cctv",
    "Tuban": "https://dishub.tubankab.go.id/cctv",
    "Lamongan": "https://dishub.lamongankab.go.id/cctv",
    "Gresik": "https://dishub.gresikkab.go.id/cctv",
    "Sidoarjo": "https://dishub.sidoarjokab.go.id/cctv",
    "Jombang": "https://dishub.jombangkab.go.id/cctv",
    "Nganjuk": "https://dishub.nganjukkab.go.id/cctv",
    "Madiun Kab": "https://dishub.madiunkab.go.id/cctv",
    "Ngawi": "https://dishub.ngawikab.go.id/cctv",
    "Magetan": "https://dishub.magetankab.go.id/cctv",
    "Ponorogo": "https://dishub.ponorogokab.go.id/cctv",
    "Pacitan": "https://dishub.pacitankab.go.id/cctv",
    "Trenggalek": "https://dishub.trenggalekkab.go.id/cctv",
    "Tulungagung": "https://dishub.tulungagungkab.go.id/cctv",
    "Kediri Kab": "https://dishub.kedirikab.go.id/cctv",
    "Blitar Kab": "https://dishub.blitarkab.go.id/cctv",
    "Malang Kab": "https://dishub.malangkab.go.id/cctv",
    "Lombok Barat": "https://dishub.lombokbaratkab.go.id/cctv",
    "Lombok Tengah": "https://dishub.lomboktengahkab.go.id/cctv",
    "Lombok Timur": "https://dishub.lomboktimurkab.go.id/cctv",
    "Sumbawa": "https://dishub.sumbawakab.go.id/cctv",
    "Bima": "https://dishub.bimakab.go.id/cctv",
    "Dompu": "https://dishub.dompukab.go.id/cctv"
}

def clear_screen():
    """Membersihkan layar terminal"""
    os.system('cls' if os.name == 'nt' else 'clear')

def typewriter_effect(text, delay=0.03):
    """Efek mengetik untuk teks"""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def animate_loading(text, duration=2):
    """Animasi loading"""
    symbols = ['⣾', '⣽', '⣻', '⢿', '⡿', '⣟', '⣯', '⣷']
    end_time = time.time() + duration
    i = 0
    while time.time() < end_time:
        print(f"\r{text} {symbols[i % len(symbols)]}", end='', flush=True)
        time.sleep(0.1)
        i += 1
    print("\r" + " " * (len(text) + 2) + "\r", end='', flush=True)

def print_header():
    """Mencetak header yang menarik"""
    clear_screen()
    print("\033[1;36m" + "="*70)
    print("🛰️" + " "*25 + "CCTV EXPLORER BY PAAN" + " "*25 + "🛰️")
    print("="*70 + "\033[0m")
    print()
    typewriter_effect("\033[1;33mSelamat datang di CCTV Explorer by Paan!\033[0m")
    typewriter_effect("Aplikasi untuk mengakses CCTV live dari berbagai kota di Indonesia")
    print()

def show_kota_available():
    """Menampilkan daftar kota yang tersedia dengan format yang menarik"""
    print("\033[1;32mDaftar Kota yang Tersedia:\033[0m")
    print("-" * 50)
    
    # Membagi daftar kota menjadi 3 kolom untuk tampilan yang lebih rapi
    kota_list = list(cctv_urls.keys())
    col_width = max(len(kota) for kota in kota_list) + 2
    num_cols = 3
    num_rows = (len(kota_list) + num_cols - 1) // num_cols
    
    for i in range(num_rows):
        row = ""
        for j in range(num_cols):
            idx = i + j * num_rows
            if idx < len(kota_list):
                kota = kota_list[idx]
                row += f"📍 {kota:<{col_width}}"
        print(row)
    print("-" * 50)

def get_cctv_link():
    """Fungsi utama untuk menampilkan link berdasarkan input kota"""
    while True:
        print_header()
        show_kota_available()
        
        print("\n\033[1;35mPilihan:\033[0m")
        print("1. Masukkan nama kota")
        print("2. Keluar")
        
        pilihan = input("\n\033[1;34mPilih opsi (1/2): \033[0m").strip()
        
        if pilihan == "2":
            print("\n\033[1;33mTerima kasih telah menggunakan CCTV Explorer by Paan! 👋\033[0m")
            break
        elif pilihan == "1":
            kota = input("\n\033[1;34mMasukkan nama kota: \033[0m").strip().title()
            
            if kota in cctv_urls:
                animate_loading("Mencari CCTV untuk kota " + kota)
                url = cctv_urls[kota]
                print(f"\n\033[1;32m✓ Berhasil menemukan CCTV untuk {kota}!\033[0m")
                print(f"\033[1;36mBerikut Link Nya Tuan: {url}\033[0m")
                
                # Konfirmasi sebelum membuka browser
                buka = input("\n\033[1;33mBuka link di browser? (y/n): \033[0m").strip().lower()
                if buka == 'y' or buka == 'yes':
                    print("\nMembuka browser...")
                    webbrowser.open(url)
                
                input("\nTekan Enter untuk melanjutkan...")
            else:
                print(f"\n\033[1;31m❌ Kota '{kota}' tidak ditemukan dalam daftar.\033[0m")
                print("Silakan periksa penulisan atau pilih kota lain.")
                input("\nTekan Enter untuk melanjutkan...")
        else:
            print("\n\033[1;31m❌ Pilihan tidak valid. Silakan pilih 1 atau 2.\033[0m")
            input("\nTekan Enter untuk melanjutkan...")

# Menjalankan aplikasi
if __name__ == "__main__":
    try:
        get_cctv_link()
    except KeyboardInterrupt:
        print("\n\n\033[1;33mAplikasi dihentikan. Terima kasih telah menggunakan CCTV Explorer by Paan! 👋\033[0m")
