angka1_1001 = int(input("Input angka-1_1001: "))
angka2_1001 = int(input("Input angka-2_1001:"))

#Penjumlahan
hasil_1001 = angka1_1001 + angka2_1001
print("\nOperator Penjumlahan")
print("Hasil_1001 =", hasil_1001)

#Pengurangan
hasil_1001 = angka1_1001 - angka2_1001
print("\nOperator Pengurangan")
print("Hasil_1001 =", hasil_1001)

#Perkalian
hasil_1001 = angka1_1001 * angka2_1001
print("\nOperator Perkalian")
print("Hasil =", hasil_1001)

#Pembagian, pembagian bulat dan sisa bagi
if angka2_1001 !=0:
    hasil = angka1_1001 /angka2_1001
    print("\nOperator Pembagian")
    print("Hasil_1001 =", hasil_1001)

    hasil = angka1_1001 // angka2_1001
    print("\nOperator Pembagian Bulat")
    print("Hasil_1001 =", hasil_1001)

    hasil_1001 = angka1_1001 % angka2_1001
    print("\nOperator Sisa Bagi")
    print("Hasil_1001 =", hasil_1001)
else:
    print("Angka kedua tidak boleh bernilai 0,")

#Pangkat
hasil_1001 = angka1_1001 ** angka2_1001
print("\nOperator pangkat")
print("Hasil_1001 =", hasil_1001)