print ("=== SISTEM REGISTRASI PRAKTIKAN ALPRO 2026 ===")

nama_1001 = input(str("Masukkan Nama Mahasiswa : "))
jenis_kelamin_1001 = input ("Masukkan Jenis Kelamin (L/P) : ")
umur_1001 = int(input("Masukkan Umur : "))
skor_tes_awal_1001 = float(input("Masukkan Skor Tes Awal : "))

print("\n=== DATA PRAKTIKAN & HASIL PEMERIKSAAN ===")

alamat_1001 = """
Andalas Residance,
Limau Manis, Kecamatan Pauh, Kota Padang, Sumatera Barat, Indonesia ,
Kota Padang """
id_token_sinyal = 100+3j

print("Nama Mahasiswa :", nama_1001, "|", "Tipe :", type(nama_1001))
print("Jenis Kelamin :", jenis_kelamin_1001, "|", "Tipe :", type(jenis_kelamin_1001))
print("Alamat Domisili :", alamat_1001, "|", "Tipe :", type(alamat_1001))
print("Umur :", umur_1001, "tahun", "|", "Tipe :", type(umur_1001))
print("Skor Tes Awal :", skor_tes_awal_1001, "|", "Tipe :", type (skor_tes_awal_1001))
print("ID Token Sinyal :", id_token_sinyal, "|", "Tipe :", type (id_token_sinyal))

print("\n=== STATUS KELULUSAN PRAKTIKUM ===")

batas_1001 = 75.0

print("Batas Minimum Nilai:", batas_1001)
if skor_tes_awal_1001 >= batas_1001:
    hasil_1001 = True
else:
    hasil_1001 = False
print("Apakah dinyatakan lulus?:", hasil_1001, "|", "Tipe :", type (hasil_1001))