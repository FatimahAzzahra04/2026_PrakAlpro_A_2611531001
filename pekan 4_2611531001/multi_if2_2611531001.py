# Input dari user
total_belanja_1001 = float(input("Masukkan total belanja (Rp): "))

# Input dari status member ( mengecek apakah user mengetik 'y' atau 'ya')
input_member_1001 = input("Apakah anda member (y/t): ").strip().lower()
is_member_1001 = input_member_1001 in ["y", "ya"]

# Input status kode promo (mengecek apakah user mengetik 'y' atau 'ya')
input_promo_1001 = input("Apakah kode promo valid? (y/t):").strip().lower()
kode_promo_valid_1001 = input_promo_1001 in["y", "ya"]

total_diskon_persen_1001 = 0

if total_belanja_1001 > 10000000:
    total_diskon_persen_1001 +=10 #Diskon belanja besar

if is_member_1001:
    total_diskon_persen_1001 += 5 #Diskon member

if kode_promo_valid_1001:
    total_diskon_persen_1001 +=15 #Diskon voucher

#Menghitung nominal diskon dan total bayar
nominal_diskon_1001 = total_belanja_1001 * (total_diskon_persen_1001 / 100)
total_bayar_1001 = total_belanja_1001 - nominal_diskon_1001

#Output hasil
print("/n--- Rincian Pembayaran ---")
print(f"Total Diskon : {total_diskon_persen_1001}%(Rp{nominal_diskon_1001:,.0f})")
print(f"Total Bayar : Rp {total_bayar_1001: ,.0f}")

print(f"Total diskon yang anda dapatkan: {total_diskon_persen_1001}%")
# Output total diskon yang anda dapatkan : 30% jika belanja > 1juta, member, dan kode promo valid