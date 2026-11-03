print("\n======================")
print("3. OPERATOR BITWISE")
print("========================")

angka1_1001 = int(input("Masukkan angka bitwise-1_1001:"))
angka2_1001 = int(input("Masukkan angka bitwise-2_1001:"))

print("\nAngka dalam bentuk desimal dan biner")
print("angka1_1001 =", angka1_1001, "| biner =" , bin(angka1_1001))
print("angka2_1001 =", angka2_1001, "| biner =", bin(angka2_1001))

#Bitwise AND
hasil_1001 = angka1_1001 & angka2_1001
print("\nBitwise AND (&)")
print(angka1_1001, "&" , angka2_1001, "=", hasil_1001 )
print("Biner hasil_1001 =", bin(hasil_1001))
print("Biner hasil (8 bit) =", format(hasil_1001, "08b"))

#Bitwise AND
hasil = angka1_1001 & angka2_1001
print("\nBitwise AND (&)")
print("Biner hasil=", bin(hasil))
print("Biner hasil (8 bit) =", format(hasil, "08b"))

#Bitwise OR
hasil = angka1_1001 | angka2_1001
print("\nbitwise or (|)")
print(angka1_1001, "|", angka2_1001, "=", hasil_1001)
print("Biner hasil_1001 =", format(hasil_1001,"08b"))

#Bitwise XOR
hasil = angka1_1001 ^ angka2_1001
print("\nbitwise XOR (^)")
print(angka1_1001, "^", angka2_1001, "=",hasil_1001)
print("Boner hasil_1001 =", bin(hasil_1001))
print("Biner hasil_1001 (8 bit) =", format(hasil_1001, "08b"))

#Bitwise NOT
hasil_1001 = -angka1_1001
print("\nBitwise NOT (-)")
print("-", angka1_1001, "=", hasil_1001)
print("Biner hasil_1001 (8 bit) =", format (hasil_1001, "08b"))

#Bitwise geser kiri
jumlah_geser_1001 = int(input("\nMasukkan jumlah pergeseran bit:"))

hasil_1001 = angka1_1001 << jumlah_geser_1001
print("\nBitwise geser kiri(<<)")
print(angka1_1001, "<<", jumlah_geser_1001,"=", hasil_1001)
print("Biner hasil_1001 (8 bit) =", format(hasil, "08b"))

#Bitwise geser kanan
hasil_1001 = angka1_1001 >> jumlah_geser_1001
print("\nBitwise geser kanan(>>)")
print(angka1_1001, ">>", jumlah_geser_1001, "=",hasil_1001)
print("Biner hasil_1001 =", bin(hasil_1001))
print("Biner hasil_1001 (8 bit_) =", format(hasil_1001, "08b"))