# Deklarasi variabel
nama = "Amir"         # Tipe data: String
umur = 17                 # Tipe data: Integer
tinggi_badan = 170.5      # Tipe data: Float
sudah_lulus = False       # Tipe data: Boolean

# Cetak informasi awal
print("=== Data Siswa ===")
print("Nama:", nama)
print("Umur:", umur, "tahun")
print("Tinggi Badan:", tinggi_badan, "cm")
print("Status Kelulusan:", "Lulus" if sudah_lulus else "Belum Lulus")

# Operasi aritmatika
tahun_sekarang = 2025
tahun_lahir = tahun_sekarang - umur   # Menghitung tahun lahir

# Cek tinggi ideal (misalnya ideal > 165 cm)
tinggi_ideal = tinggi_badan > 165

# Logika kelulusan dan tinggi badan
boleh_ikut_wisuda = sudah_lulus and tinggi_ideal

# Output hasil pengolahan data
print("\n=== Hasil Pengolahan Data ===")
print("Tahun Lahir:", tahun_lahir)
print("Apakah tinggi badan ideal?", tinggi_ideal)
print("Boleh ikut wisuda?", boleh_ikut_wisuda)
