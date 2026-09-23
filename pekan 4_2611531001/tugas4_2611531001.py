print("=== SISTEM LOKET ALPRO ADVENTURE PARK ===")

# 1. Input Data Pengunjung Utama
nama_1001 = input("Masukkan Nama Pengunjung        : ")
umur_1001 = int(input("Input umur anda                 : "))
sim_1001 = input("Apakah Anda Sudah Punya SIM C (y/t): ")[0].lower()

# Status Kepemilikan SIM
status_sim_1001 = "Punya" if sim_1001 == 'y' else "Tidak Punya"

#Output biodata pengunjung
print("\n-----------------------------------------")
print("--- BIODATA PENGUNJUNG ---")
print(f"Nama Pengunjung  : {nama_1001}")
print(f"Umur             : {umur_1001} tahun")
print(f"Status SIM C     : {status_sim_1001}")

# Tampilkan Daftar Paket Wahana untuk Masukan Pengunjung
print("\nPilihan Paket Wahana (1-5):")
print("  1. Safari Rimba         (Rp 50,000)")
print("  2. Arung Jeram          (Rp 75,000)")
print("  3. Motor ATV Ekstrim    (Rp 120,000)")
print("  4. Roller Coaster Kilat (Rp 100,000)")
print("  5. All-Access VIP       (Rp 220,000)")

paket_1001 = int(input("Masukkan nomor paket (1-5)      : "))
jumlah_tiket_1001 = int(input("Masukkan jumlah tiket           : "))

# Penerapan IF tunggal untuk validasi kuota tiket
if jumlah_tiket_1001 <= 0:
    print("Peringatan: Kuota tiket tidak valid!")

input_member_1001 = input("Apakah Anda member? (y/t)        : ").strip().lower()
is_member_1001 = input_member_1001 in [ "y", "ya"]

input_promo_1001 = input("Apakah kode promo valid? (y/t)  : ").strip().lower()
kode_promo_valid_1001 = input_promo_1001 in [ "y", "ya"]

# 2. Pemilihan Wahana Menggunakan match-case
harga_satuan_1001 = 0
nama_wahana_1001 = ""

match paket_1001:
    case 1:
        nama_wahana_1001 = "Wahana Safari Rimba"
        harga_satuan_1001 = 50000
    case 2:
        nama_wahana_1001 = "Wahana Arung Jeram"
        harga_satuan_1001 = 75000
    case 3:
        nama_wahana_1001 = "Wahana Motor ATV Ekstrim"
        harga_satuan_1001 = 120000
    case 4:
        nama_wahana_1001 = "Wahana Roller Coaster Kilat"
        harga_satuan_1001 = 100000
    case 5:
        nama_wahana_1001 = "Wahana All-Access VIP"
        harga_satuan_1001 = 220000
    case _:
        print("\nPaket wahana tidak valid!")
        harga_satuan_1001 = 0

if harga_satuan_1001 > 0 and jumlah_tiket_1001 > 0:

    # 3. Validasi Izin Kendali Wahana Menggunakan if-elif-else
    print("\n--- KELAYAKAN PENGENDARA WAHANA ---")
    if paket_1001 == 3:
        if umur_1001 >= 17 and sim_1001 == 'y':
            status_akses_1001 = "Anda sudah dewasa dan boleh mengendarai ATV sendiri."
        elif umur_1001 >= 17 and sim_1001 != 'y':
            status_akses_1001 = "Anda sudah dewasa tetapi tidak boleh bawa motor ATV (wajib didampingi instruktur)."
        elif umur_1001 < 17 and sim_1001 == 'y':
            status_akses_1001 = "Identitas tidak valid: Belum cukup umur memiliki SIM."
        else:
            status_akses_1001 = "Anda belum cukup umur dan tidak boleh bawa motor ATV."
    else:
        if umur_1001 >= 10:
            status_akses_1001 = "Anda memenuhi syarat umur untuk wahana ini."
        else:
            status_akses_1001 = "Anda belum cukup umur untuk wahana ini."

    print(f"Status Akses: {status_akses_1001}")

    # 4. Akumulasi Diskon Bertingkat Menggunakan Multi-IF Terpisah
    subtotal_1001 = harga_satuan_1001 * jumlah_tiket_1001
    total_diskon_persen_1001 = 0

    if subtotal_1001 >= 200000:
        total_diskon_persen_1001 += 10  # Diskon Belanja Besar

    if is_member_1001:
        total_diskon_persen_1001 += 5   # Diskon Member

    if kode_promo_valid_1001:
        total_diskon_persen_1001 += 15  # Diskon Voucher Promo

    if jumlah_tiket_1001 >= 5:
        total_diskon_persen_1001 += 5   # Diskon Tambahan Rombongan

    # 5. Menghitung Nominal Diskon dan Total Bayar
    nominal_diskon_1001 = subtotal_1001 * (total_diskon_persen_1001 / 100)
    total_bayar_1001 = subtotal_1001 - nominal_diskon_1001

    # Evaluasi Bonus Audit Menggunakan if-else
    if total_bayar_1001 > 300000:
        catatan_layanan_1001 = "Selamat! Anda berhak mendapatkan Souvenir Gratis."
    else:
        catatan_layanan_1001 = "Terima kasih telah berkunjung."

    # OUTPUT SELANJUTNYA: RINCIAN PEMBAYARAN
    print("\n--- RINCIAN PEMBAYARAN ---")
    print("\n--- DETAIL TRANSAKSI & PEMBAYARAN ---")
    print(f"Paket Dipilih    : Paket {paket_1001} ({nama_wahana_1001})")
    print(f"Jumlah Tiket     : {jumlah_tiket_1001} tiket")
    print(f"Status Member    : {input_member_1001}")
    print(f"Kode Promo Valid : {input_promo_1001}")
    print(f"Wahana Dipilih   : {nama_wahana_1001}")
    print(f"Jumlah Tiket     : {jumlah_tiket_1001} tiket")
    print(f"Subtotal Belanja : Rp {subtotal_1001:,.0f}")
    print(f"Total Diskon     : {total_diskon_persen_1001}% (Rp {nominal_diskon_1001:,.0f})")
    print(f"Total Bayar      : Rp {total_bayar_1001:,.0f}")
    print(f"Catatan Layanan  : {catatan_layanan_1001}")

print("Program Selesai")