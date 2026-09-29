ulang_1001 = int(input("Masukkan jumlah perulangan:"))

jumlah_1001=0
for i  in range(1, ulang_1001 + 1):
    print(i, end=" ")
    jumlah_1001 = jumlah_1001 + i

    if i < ulang_1001:
        print("+", end= " ")
    else:
        print("-", jumlah_1001, end= " ")
print()
print("Jumlah =", jumlah_1001)