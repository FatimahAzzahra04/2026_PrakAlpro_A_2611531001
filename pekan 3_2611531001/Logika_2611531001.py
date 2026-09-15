a1_1001 = input("input nilai boolean-1_1001 (true/false): ").strip().lower() == "true"
a2_1001 = input("input nilai boolean-2_1001 (true/false): ").strip().lower() == "true"

print("\nA1_1001 =" , a1_1001)
print("A2_1001 =" , a2_1001)

#Konjungsi: bernilai True jika True
hasil_1001 = a1_1001 and a2_1001
print("\nKonjungsi (AND)")
print("A1_1001 and A2_1001 =", hasil_1001)

#Disjungsi: bernilai True jika salah satunya True
hasil_1001 = a1_1001 or a2_1001
print("\nDisjungsi (OR)")
print("A1_1001 or A2_1001 =", hasil_1001)

#Negasi A1_1001: membalik niali A1_1001
hasil = not a1_1001
print("\nNegasi A1_1001 (NOT)")
print("not A2_1001 =", hasil_1001)

#Negasi A2_1001: membalik nilai A2_1001
hasil = not a2_1001
print("\nNegasi A2 (NOT)")
print("not A2_1001 =", hasil_1001)

#XOR: bernilai True jika kedua niali berbeda
hasil_1001 = a1_1001 != a2_1001
print("\nDisjungsi Eksklusif (XOR)")
print("A1_1001 XOR A2_1001 =", hasil_1001)