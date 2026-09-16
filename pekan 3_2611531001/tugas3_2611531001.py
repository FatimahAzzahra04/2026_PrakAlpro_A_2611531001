
# Daftar Kode Promo Terdaftar
daftar_promo_1001 = ["HEMAT10", "HEMAT20", "GRATISONGKIR"]

# ------------------------------------------------------------------------------
# 1. INPUT DATA PELANGGAN & TRANSAKSI
# ------------------------------------------------------------------------------
print("=== SISTEM TRANSAKSI TOKO ===\n")

nama_pelanggan_1001 = input("Masukkan Nama Pelanggan : ")
status_input_1001 = input("Masukkan Status Pelanggan (member/nonmember) : ")
total_belanja_1001 = float(input("Masukkan Total Belanja : "))
jumlah_barang_1001= int(input("Masukkan Jumlah Barang : "))
kode_promo_1001 = input("Masukkan Kode Promo : ")

# ------------------------------------------------------------------------------
# 2. OPERATOR PERBANDINGAN & KEANGGOTAAN (MEMBERSHIP)
# ------------------------------------------------------------------------------
# Operator Perbandingan: >=, ==
is_min_belanja_1001 = total_belanja_1001 >= 200000
is_min_barang_1001 = jumlah_barang_1001 >= 3
is_member_1001 = status_input_1001.lower() == "member"

# Operator Keanggotaan: in, not in
is_promo_tersedia_1001 = kode_promo_1001 in daftar_promo_1001
is_promo_bukan_sampah_1001 = kode_promo_1001 not in ["INVALID"]

# ------------------------------------------------------------------------------
# 3. OPERATOR LOGIKA
# ------------------------------------------------------------------------------
# Operator Logika: and, or, not
dapat_diskon_1001 = is_member_1001 and is_min_belanja_1001
dapat_promo_1001 = is_promo_tersedia_1001 or (is_min_barang_1001 and not (total_belanja_1001 < 100000))

# ------------------------------------------------------------------------------
# 4. OPERATOR ARITMATIKA & PENUGASAN (ASSIGNMENT)
# ------------------------------------------------------------------------------
# Operator Aritmatika: *, /, -, %
persen_diskon_1001 = 0.10 if dapat_diskon_1001 else 0.0
besarnya_diskon_1001 = total_belanja_1001 * persen_diskon_1001
rata_harga_barang_1001 = total_belanja_1001 / jumlah_barang_1001
sisa_pembagian_barang_1001 = jumlah_barang_1001 % 2  

# Operator Penugasan (Augmented Assignment): -=, +=
total_pembayaran_1001 = total_belanja_1001
total_pembayaran_1001 -= besarnya_diskon_1001

poin_pelanggan_1001 = 0
poin_pelanggan_1001 += int(total_pembayaran_1001 / 10000)  

# ------------------------------------------------------------------------------
# 5. OPERATOR IDENTITAS (IDENTITY)
# ------------------------------------------------------------------------------
# Operator Identitas: is, is not
list_promo1_1001 = ["HEMAT10", "HEMAT20", "GRATISONGKIR"]
list_promo2_1001 = ["HEMAT10", "HEMAT20", "GRATISONGKIR"]
list_promo3_1001 = list_promo1_1001

is_objek_berbeda_1001 = list_promo1_1001 is not list_promo2_1001  
is_objek_sama_1001 = list_promo1_1001 is list_promo3_1001

# ------------------------------------------------------------------------------
# 6. OPERATOR BITWISE
# ------------------------------------------------------------------------------
# Bit 0 (0001) = Member
# Bit 1 (0010) = Belanja >= 200.000
# Bit 2 (0100) = Barang >= 3
# Bit 3 (1000) = Promo Tersedia

bit0_1001 = 1 if is_member_1001 else 0
bit1_1001 = 2 if is_min_belanja_1001 else 0
bit2_1001 = 4 if is_min_barang_1001 else 0
bit3_1001 = 8 if is_promo_tersedia_1001 else 0

# Bitwise OR (|) - Menggabungkan status
status_bit_1001 = bit0_1001 | bit1_1001 | bit2_1001 | bit3_1001

# Bitwise AND (&) - Pemeriksaan status
cek_member_1001 = status_bit_1001 & 1
cek_promo_1001 = status_bit_1001 & 8

# Bitwise XOR (^) - Perbandingan perbedaan (Kode Referensi 1011 = 11)
kode_promo_1001= 11
hasil_xor_1001 = status_bit_1001 ^ kode_promo_1001

# Bitwise Shift Left (<<)
hasil_shift_1001 = status_bit_1001 << 1

# ------------------------------------------------------------------------------
# OUTPUT PROGRAM
# ------------------------------------------------------------------------------
print("\n=== DATA TRANSAKSI ===")
print("Nama Pelanggan :", nama_pelanggan_1001)
print("Status Pelanggan :",status_input_1001)
print("Total Belanja  :Rp",   int(total_belanja_1001))
print("Jumlah Barang :", jumlah_barang_1001)
print("Kode Promo  :", kode_promo_1001)

print("\n=== HASIL VALIDASI ===")
print("Belanja >= Rp200000 :",is_min_belanja_1001)
print("Jumlah Barang >= 3 :",is_min_barang_1001)
print("Status Member  :",is_member_1001)
print("Kode Promo Tersedia :", is_promo_tersedia_1001)
print("Mendapatkan Diskon  :",dapat_diskon_1001)
print("Mendapatkan Promo  :",dapat_promo_1001)

print("\n=== HASIL PERHITUNGAN ===")
print("Diskon :Rp", int(besarnya_diskon_1001))
print("Total Pembayaran :Rp", int(total_pembayaran_1001))
print("Rata-rata Harga Barang  :Rp", int(rata_harga_barang_1001))

print("\n=== HAK AKSES PELANGGAN ===")
print("Kode Hak Akses  :", format(status_bit_1001, "04b"))
print("Member Access  :", bool(cek_member_1001))
print("Promo Access  :", bool(cek_promo_1001))
print("Free Shipping Access :", kode_promo_1001 == 'GRATISONGKIR')

print("\n=== OPERASI BITWISE ===")
print("=== Kode Status Transaksi ===")
print("0001 | 0010 | 0100 | 1000")
print("Kode Biner :", format(status_bit_1001, "04b"))
print("Kode Desimal :", status_bit_1001)

print("\n=== Pemeriksaan Status ===")
print("Cek Member")
print(format(status_bit_1001, '04b'), "& 0001")
print("Hasil Biner :", format(cek_member_1001, "04b"))
print("Hasil Desimal :", cek_member_1001)

print("\nCek Promo")
print("bin(status_bit_1001) & 1000")
print("Hasil Biner :", format(cek_promo_1001, "04b"))
print("Hasil Desimal :", cek_promo_1001)

print("\n=== Perbandingan Status ===")
print("Kode Transaksi :", status_bit_1001 )
print("Kode Referensi :", kode_promo_1001 )
print(format(status_bit_1001, "04b"), " ^ ", format(kode_promo_1001, "04b"))
print("Hasil Biner :", format(hasil_xor_1001, "04b"))
print("Hasil Desimal :", hasil_xor_1001)

print("\n=== Shift ===")
print(format(status_bit_1001, "04b") ,"<< 1")
print("Hasil Biner :",format(hasil_shift_1001, "04b")) 
print("Hasil Desimal :", hasil_shift_1001)

print("\n=== SELESAI ===")

