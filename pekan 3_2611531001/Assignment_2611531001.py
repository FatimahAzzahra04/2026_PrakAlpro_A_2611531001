angka1_1001 = int(input("input angka-1_1001: " ))
angka2_1001 = int(input("input angka-2_1001: " ))

print("\nNilai awal angka1_1001 =" , angka1_1001)
print("Nilai angka2_1001 =" , angka2_1001)

#Assignment biasa 
hasil_1001 = angka1_1001
print("\nAssignment biasa (=)")
print("Hasil_1001 =", hasil_1001)

#Assignment penambahan 
hasil_1001 = angka1_1001
hasil_1001 += angka2_1001
print("Hasil_1001 =", hasil_1001)

#Assignment pengurangan
hasil_1001 =angka1_1001
hasil_1001 -= angka2_1001
print("\nAssignment pengurangan (-=)")
print("Hasil_1001 =", hasil_1001)

#Assignment perkalian
hasil_1001 = angka1_1001
hasil_1001 *= angka2_1001
print("\nAssignment perkalian (*=)")
print("Hasil_1001 =", hasil_1001)
      
#Assignment pembagian, pembagian bulat, dan sisa bagi
if angka2_1001 != 0:
    hasil_1001 = angka1_1001
    hasil_1001 /= angka2_1001
    print("\nAssignment pembagian (/=)")
    print("Hasil_1001 =", hasil_1001)
    # Operator tambahan
    hasil_1001 = angka1_1001
    hasil_1001 //= angka2_1001
    print("\nAssignment pembagian bulat  (//=)")
    print("Hasil_1001 =", hasil_1001)
    hasil_1001 = angka1_1001
    hasil_1001 %= angka2_1001
    print("\nAssignment sisa bagi (%=)")
    print("Hasil_1001 =", hasil_1001)
else:
    print("\nPembagian tidak dapat dilakukan")
    print("Angka kedua tidak boleh bernilai 0")

#Operator tambahan : assignment perpangkatan
hasil_1001 = angka1_1001
hasil_1001 **= angka2_1001
print("\nAssignment perpangkatan(**=)")
print("Hasil_1001 =", hasil_1001)
          

    