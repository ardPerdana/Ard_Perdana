import json
import datetime
from typing import List, Dict, Any
import random

class MalangSmartTourismGuide:
    def __init__(self):
        self.tempat_wisata = self._load_tempat_wisata()
        self.kuliner = self._load_kuliner()
        self.acara_khusus = self._load_acara_khusus()
        self.user_preferences = {}
    
    def _load_tempat_wisata(self) -> List[Dict[str, Any]]:
        """Memuat data tempat wisata di Malang"""
        return [
            {
                "id": 1,
                "nama": "Alun-Alun Malang",
                "kategori": ["Sejarah", "Keluarga"],
                "deskripsi": "Pusat kota Malang dengan taman yang indah dan air mancur menari",
                "lokasi": "Pusat Kota",
                "waktu_buka": "06:00-22:00",
                "harga_tiket": "Gratis",
                "rating": 4.5,
                "fasilitas": ["Toilet", "Parkir", "WiFi", "Area Bermain Anak"]
            },
            {
                "id": 2,
                "nama": "Museum Brawijaya",
                "kategori": ["Sejarah", "Edukasi"],
                "deskripsi": "Museum yang menyimpan sejarah perjuangan di Malang",
                "lokasi": "Jl. Ijen",
                "waktu_buka": "08:00-16:00",
                "harga_tiket": "Rp 5.000",
                "rating": 4.2,
                "fasilitas": ["Toilet", "Parkir", "Pemandu"]
            },
            {
                "id": 3,
                "nama": "Kampung Warna-Warni Jodipan",
                "kategori": ["Foto", "Budaya"],
                "deskripsi": "Kampung dengan rumah-rumah berwarna-warni yang instagramable",
                "lokasi": "Jodipan",
                "waktu_buka": "24 jam",
                "harga_tiket": "Gratis",
                "rating": 4.7,
                "fasilitas": ["Toilet", "Spot Foto"]
            },
            {
                "id": 4,
                "nama": "Alun-Alun Tugu",
                "kategori": ["Sejarah", "Keluarga"],
                "deskripsi": "Alun-alun dengan Tugu Malang yang ikonik",
                "lokasi": "Pusat Kota",
                "waktu_buka": "24 jam",
                "harga_tiket": "Gratis",
                "rating": 4.4,
                "fasilitas": ["Parkir", "Area Duduk", "Penerangan"]
            },
            {
                "id": 5,
                "nama": "Selecta",
                "kategori": ["Alam", "Keluarga"],
                "deskripsi": "Taman rekreasi dengan pemandangan Gunung Arjuna",
                "lokasi": "Batu",
                "waktu_buka": "08:00-17:00",
                "harga_tiket": "Rp 40.000",
                "rating": 4.6,
                "fasilitas": ["Kolam Renang", "Wahana Bermain", "Penginapan", "Restoran"]
            }
        ]
    
    def _load_kuliner(self) -> List[Dict[str, Any]]:
        """Memuat data kuliner khas Malang"""
        return [
            {
                "id": 1,
                "nama": "Bakso President",
                "jenis": "Bakso",
                "deskripsi": "Bakso terkenal dengan pilihan bakso isi yang beragam",
                "lokasi": "Jl. Batanghari",
                "harga": "Rp 25.000 - Rp 50.000",
                "rating": 4.8,
                "rekomendasi": ["Bakso Isi Telur", "Bakso Urat"]
            },
            {
                "id": 2,
                "nama": "Warung Pojok",
                "jenis": "Nasi Campur",
                "deskripsi": "Nasi campur khas Malang dengan lauk-pauk lengkap",
                "lokasi": "Jl. Kahuripan",
                "harga": "Rp 20.000 - Rp 35.000",
                "rating": 4.6,
                "rekomendasi": ["Nasi Campur Spesial", "Sate Usus"]
            },
            {
                "id": 3,
                "nama": "Cak Man",
                "jenis": "Sate",
                "deskripsi": "Sate ayam dengan bumbu kacang khas Malang",
                "lokasi": "Jl. Kertanegara",
                "harga": "Rp 15.000 - Rp 30.000",
                "rating": 4.7,
                "rekomendasi": ["Sate Ayam", "Es Teh"]
            },
            {
                "id": 4,
                "nama": "Rumah Makan Lembah Dieng",
                "jenis": "Masakan Jawa",
                "deskripsi": "Restoran dengan pemandangan indah dan masakan Jawa autentik",
                "lokasi": "Jl. Dieng",
                "harga": "Rp 40.000 - Rp 100.000",
                "rating": 4.5,
                "rekomendasi": ["Gurame Bakar", "Sayur Asem"]
            },
            {
                "id": 5,
                "jenis": "Jajanan",
                "nama": "Pisang Nugget",
                "deskripsi": "Olahan pisang khas Malang yang digoreng dengan tepung",
                "lokasi": "Berbagai lokasi",
                "harga": "Rp 10.000 - Rp 20.000",
                "rating": 4.4,
                "rekomendasi": ["Pisang Coklat", "Pisang Keju"]
            }
        ]
    
    def _load_acara_khusus(self) -> List[Dict[str, Any]]:
        """Memuat data acara khusus di Malang"""
        return [
            {
                "nama": "Malang Night Carnival",
                "deskripsi": "Karnaval malam dengan kostum warna-warni",
                "waktu": "Oktober",
                "lokasi": "Jl. Ijen"
            },
            {
                "nama": "Festival Malang Kembali",
                "deskripsi": "Festival budaya dan sejarah kota Malang",
                "waktu": "Agustus",
                "lokasi": "Alun-Alun Malang"
            },
            {
                "nama": "Batu Night Spectacular",
                "deskripsi": "Pertunjukan lampu dan wahana malam",
                "waktu": "Setiap hari",
                "lokasi": "Batu"
            }
        ]
    
    def set_user_preferences(self, minat: List[str], budget: str, durasi: int, kelompok: str):
        """Menyimpan preferensi pengguna"""
        self.user_preferences = {
            "minat": minat,
            "budget": budget,
            "durasi": durasi,  # dalam jam
            "kelompok": kelompok
        }
        print("Preferensi berhasil disimpan!")
    
    def rekomendasi_tempat_wisata(self) -> List[Dict[str, Any]]:
        """Memberikan rekomendasi tempat wisata berdasarkan preferensi"""
        if not self.user_preferences:
            print("Silakan atur preferensi terlebih dahulu!")
            return []
        
        minat = self.user_preferences.get("minat", [])
        budget = self.user_preferences.get("budget", "sedang")
        
        # Filter berdasarkan minat
        filtered = []
        for tempat in self.tempat_wisata:
            for kategori in tempat["kategori"]:
                if kategori in minat:
                    filtered.append(tempat)
                    break
        
        # Filter berdasarkan budget jika diperlukan
        if budget == "rendah":
            filtered = [t for t in filtered if "Gratis" in t["harga_tiket"] or int(t["harga_tiket"].replace("Rp ", "").replace(".", "")) < 20000]
        elif budget == "sedang":
            filtered = [t for t in filtered if int(t["harga_tiket"].replace("Gratis", "0").replace("Rp ", "").replace(".", "")) < 50000]
        
        # Urutkan berdasarkan rating
        filtered.sort(key=lambda x: x["rating"], reverse=True)
        
        return filtered[:3]  # Kembalikan 3 rekomendasi teratas
    
    def rekomendasi_kuliner(self) -> List[Dict[str, Any]]:
        """Memberikan rekomendasi kuliner berdasarkan preferensi"""
        if not self.user_preferences:
            print("Silakan atur preferensi terlebih dahulu!")
            return []
        
        budget = self.user_preferences.get("budget", "sedang")
        kelompok = self.user_preferences.get("kelompok", "sendiri")
        
        filtered = self.kuliner.copy()
        
        # Filter berdasarkan budget
        if budget == "rendah":
            filtered = [k for k in filtered if "Rp 10.000" in k["harga"] or "Rp 15.000" in k["harga"]]
        elif budget == "sedang":
            filtered = [k for k in filtered if not ("Rp 100.000" in k["harga"])]
        
        # Filter berdasarkan kelompok
        if kelompok == "keluarga":
            filtered = [k for k in filtered if k["jenis"] in ["Masakan Jawa", "Nasi Campur"]]
        
        # Urutkan berdasarkan rating
        filtered.sort(key=lambda x: x["rating"], reverse=True)
        
        return filtered[:3]
    
    def buat_rencana_perjalanan(self, hari: int = 1):
        """Membuat rencana perjalanan untuk jumlah hari tertentu"""
        if not self.user_preferences:
            print("Silakan atur preferensi terlebih dahulu!")
            return
        
        durasi_harian = self.user_preferences.get("durasi", 8)
        
        print(f"\n{'='*50}")
        print(f"RENCANA PERJALANAN {hari} HARI DI MALANG")
        print(f"{'='*50}")
        
        for day in range(1, hari + 1):
            print(f"\nHARI {day}:")
            
            # Pagi (3-4 jam pertama)
            print(f"\nPAGI (08:00 - 12:00):")
            tempat_pagi = self.rekomendasi_tempat_wisata()
            if tempat_pagi:
                print(f"  • Mengunjungi {tempat_pagi[0]['nama']}")
                print(f"    {tempat_pagi[0]['deskripsi']}")
            
            # Siang (makan siang)
            print(f"\nSIANG (12:00 - 14:00):")
            kuliner_siang = self.rekomendasi_kuliner()
            if kuliner_siang:
                print(f"  • Makan siang di {kuliner_siang[0]['nama']}")
                print(f"    Rekomendasi: {', '.join(kuliner_siang[0]['rekomendasi'])}")
            
            # Sore (2-3 jam)
            print(f"\nSORE (14:00 - 17:00):")
            if len(tempat_pagi) > 1:
                print(f"  • Mengunjungi {tempat_pagi[1]['nama']}")
            else:
                acara = random.choice(self.acara_khusus)
                print(f"  • {acara['nama']}")
                print(f"    {acara['deskripsi']}")
            
            # Malam
            print(f"\nMALAM (19:00 - 21:00):")
            if len(kuliner_siang) > 1:
                print(f"  • Makan malam di {kuliner_siang[1]['nama']}")
            else:
                print(f"  • Menjelajahi Alun-Alun Malang malam hari")
    
    def cari_tempat_wisata(self, keyword: str):
        """Mencari tempat wisata berdasarkan kata kunci"""
        results = []
        keyword = keyword.lower()
        
        for tempat in self.tempat_wisata:
            if (keyword in tempat["nama"].lower() or 
                keyword in tempat["deskripsi"].lower() or
                any(keyword in kat.lower() for kat in tempat["kategori"])):
                results.append(tempat)
        
        return results
    
    def info_acara_khusus(self):
        """Menampilkan informasi acara khusus di Malang"""
        print("\n" + "="*50)
        print("ACARA KHUSUS DI MALANG")
        print("="*50)
        
        bulan_sekarang = datetime.datetime.now().month
        bulan_indonesia = [
            "Januari", "Februari", "Maret", "April", "Mei", "Juni",
            "Juli", "Agustus", "September", "Oktober", "November", "Desember"
        ]
        
        for acara in self.acara_khusus:
            print(f"\n• {acara['nama']}")
            print(f"  {acara['deskripsi']}")
            print(f"  Waktu: {acara['waktu']}")
            print(f"  Lokasi: {acara['lokasi']}")
            
            # Cek jika acara bulan ini
            if acara['waktu'].lower() == bulan_indonesia[bulan_sekarang-1].lower():
                print(f"  ⭐ ACARA BULAN INI!")
    
    def tampilkan_peta_sederhana(self, lokasi: str):
        """Menampilkan peta sederhana lokasi di Malang"""
        peta = {
            "Pusat Kota": ["Alun-Alun Malang", "Alun-Alun Tugu", "Museum Brawijaya"],
            "Jodipan": ["Kampung Warna-Warni Jodipan"],
            "Batu": ["Selecta", "Batu Night Spectacular"],
            "Dieng": ["Rumah Makan Lembah Dieng"]
        }
        
        print(f"\nPeta Lokasi: {lokasi}")
        print("-" * 30)
        
        if lokasi in peta:
            for tempat in peta[lokasi]:
                print(f"📍 {tempat}")
            
            if lokasi == "Pusat Kota":
                print("\nRute: Alun-Alun Tugu → Museum Brawijaya → Alun-Alun Malang")
                print("Jarak: ± 2 km (dapat ditempuh dengan jalan kaki)")
        else:
            print("Lokasi tidak ditemukan dalam peta.")
    
    def menu_utama(self):
        """Menampilkan menu utama program"""
        while True:
            print("\n" + "="*50)
            print("MALANG SMART TOURISM GUIDE")
            print("="*50)
            print("1. Atur Preferensi Wisata")
            print("2. Rekomendasi Tempat Wisata")
            print("3. Rekomendasi Kuliner")
            print("4. Buat Rencana Perjalanan")
            print("5. Cari Tempat Wisata")
            print("6. Info Acara Khusus")
            print("7. Lihat Peta Sederhana")
            print("8. Keluar")
            
            pilihan = input("\nPilih menu (1-8): ")
            
            if pilihan == "1":
                print("\n--- Atur Preferensi Wisata ---")
                print("Kategori minat: Sejarah, Alam, Foto, Keluarga, Edukasi, Budaya")
                minat_input = input("Masukkan minat (pisahkan dengan koma): ").split(",")
                minat = [m.strip() for m in minat_input]
                
                print("\nPilihan budget: rendah, sedang, tinggi")
                budget = input("Masukkan budget: ").strip().lower()
                
                print("\nDurasi dalam jam per hari (contoh: 8)")
                durasi = int(input("Masukkan durasi: "))
                
                print("\nKelompok: sendiri, pasangan, keluarga, teman")
                kelompok = input("Masukkan jenis kelompok: ").strip().lower()
                
                self.set_user_preferences(minat, budget, durasi, kelompok)
                
            elif pilihan == "2":
                print("\n--- Rekomendasi Tempat Wisata ---")
                rekomendasi = self.rekomendasi_tempat_wisata()
                if rekomendasi:
                    for i, tempat in enumerate(rekomendasi, 1):
                        print(f"\n{i}. {tempat['nama']}")
                        print(f"   Kategori: {', '.join(tempat['kategori'])}")
                        print(f"   {tempat['deskripsi']}")
                        print(f"   Lokasi: {tempat['lokasi']}")
                        print(f"   Waktu Buka: {tempat['waktu_buka']}")
                        print(f"   Harga Tiket: {tempat['harga_tiket']}")
                        print(f"   Rating: {tempat['rating']}/5.0")
                else:
                    print("Tidak ada rekomendasi. Coba ubah preferensi.")
            
            elif pilihan == "3":
                print("\n--- Rekomendasi Kuliner ---")
                rekomendasi = self.rekomendasi_kuliner()
                if rekomendasi:
                    for i, kuliner in enumerate(rekomendasi, 1):
                        print(f"\n{i}. {kuliner['nama']}")
                        print(f"   Jenis: {kuliner['jenis']}")
                        print(f"   {kuliner['deskripsi']}")
                        print(f"   Lokasi: {kuliner['lokasi']}")
                        print(f"   Harga: {kuliner['harga']}")
                        print(f"   Rating: {kuliner['rating']}/5.0")
                        print(f"   Rekomendasi: {', '.join(kuliner['rekomendasi'])}")
                else:
                    print("Tidak ada rekomendasi. Coba ubah preferensi.")
            
            elif pilihan == "4":
                print("\n--- Buat Rencana Perjalanan ---")
                hari = int(input("Berapa hari rencana perjalanan? "))
                self.buat_rencana_perjalanan(hari)
            
            elif pilihan == "5":
                print("\n--- Cari Tempat Wisata ---")
                keyword = input("Masukkan kata kunci pencarian: ")
                hasil = self.cari_tempat_wisata(keyword)
                if hasil:
                    print(f"\nDitemukan {len(hasil)} hasil:")
                    for tempat in hasil:
                        print(f"\n• {tempat['nama']}")
                        print(f"  {tempat['deskripsi']}")
                        print(f"  Lokasi: {tempat['lokasi']}")
                else:
                    print("Tidak ditemukan tempat wisata dengan kata kunci tersebut.")
            
            elif pilihan == "6":
                self.info_acara_khusus()
            
            elif pilihan == "7":
                print("\n--- Peta Sederhana Malang ---")
                print("Lokasi yang tersedia: Pusat Kota, Jodipan, Batu, Dieng")
                lokasi = input("Masukkan lokasi yang ingin dilihat: ")
                self.tampilkan_peta_sederhana(lokasi)
            
            elif pilihan == "8":
                print("\nTerima kasih telah menggunakan Malang Smart Tourism Guide!")
                print("Selamat menikmati wisata di Malang! 🏞️")
                break
            
            else:
                print("Pilihan tidak valid. Silakan pilih 1-8.")

def main():
    """Fungsi utama untuk menjalankan program"""
    print("Selamat datang di Malang Smart Tourism Guide!")
    print("Program ini akan membantu Anda merencanakan wisata di Malang.")
    
    # Inisialisasi guide
    guide = MalangSmartTourismGuide()
    
    # Jalankan menu utama
    guide.menu_utama()

if __name__ == "__main__":
    main()