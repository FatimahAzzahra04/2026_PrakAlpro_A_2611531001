print("==============================================")
print("1. OPERATOR KEANGGOTAAN")
print("==============================================")

#Input beberapa data yang dipisahkan dengan koma
input_data_1001 = input ("Masukkan beberapa angka, pisahkan dengan koma: ")

#Mengubah input menjadi list integer
data_list_1001 = [int(angka.strip()) for angka in input_data_1001.split(",")]

nilai_dicari_1001 = int(input("Masukkan nilai yang ingin dicari:"))

# Operator in
hasil_in_1001 = nilai_dicari_1001 in data_list_1001
print("\nOperator keanggotaan IN")
print(nilai_dicari_1001, "in", data_list_1001, "=", hasil_in_1001)

# Operator not in
hasil_not_in_1001 = nilai_dicari_1001 not in data_list_1001
print("\nOperator keanggotaan NOT IN")
print(nilai_dicari_1001, "not in", data_list_1001, "=", hasil_not_in_1001)

print("\n==============================")
print("2. OPERATOR IDENTITAS")
print("================================")

#objek1 menggunakan list dari input pengguna
objek1_1001 = data_list_1001

#objek2 menggunakan list dari input pengguna
objek2_1001 =  objek1_1001

#objek3 memiliki isi sama, tetapi merupakan objek baru
objek3_1001 = data_list_1001.copy()

print("objek1_1001 =", objek1_1001)
print("objek2_1001 =", objek2_1001)
print("objek3-1001 =", objek3_1001)

#Operator is
hasil_is_1001 = objek1_1001 is objek2_1001
print("\nOperator identitas IS")
print("objek1_1001 is objek2_10001 =", hasil_is_1001)

#Operator is not
hasil_is_not_1001 = objek1_1001 is not objek2_1001
print("\nOperator identitas IS NOT")
print("objek1_1001 is not objek3_1001 =", hasil_is_not_1001)

#Perbandingan identitas dan nilai
print("\nPerbandingan identitas dan nilai")
print("objek1_1001 is objek3_1001 =", objek1_1001 is objek3_1001)
print("objek1_1001 == objek3_1001 =", objek1_1001 == objek3_1001)