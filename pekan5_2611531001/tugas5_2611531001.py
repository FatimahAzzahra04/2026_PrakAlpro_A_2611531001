print("=== PROGRAM JAM PASIR KRISTAL PALINDROMI ===")
n_1001 = int(input("Masukkan ukuran skala jam pasir (N): "))

#-------Bingkai atas------
print("#", end="")
for i_1001 in range(4 * n_1001 + 5):
    print("=", end="")
print("#")

#------Fase 1 Angka menurun (baris N -> 1)------
for baris_1001 in range(n_1001, 0, -1):
    print("| ", end="")
    for spasi_1001 in range(2 * (n_1001 - baris_1001)):
        print(" ", end="")
    for angka_1001 in range(baris_1001, 0, -1):
        print(angka_1001, end=" ")
    print("<*>", end="")
    for angka_1001 in range(1, baris_1001 + 1):
        print(" ", end="")
        print(angka_1001, end="")
    for spasi_1001 in range(2 * (n_1001 - baris_1001)):
        print(" ", end="")
    print(" |", end="")
    print()

#--------Fase 2 Poros titik pusat------
print("|", end="")
for spasi_1001 in range(2 * n_1001 + 1):
    print(" ", end="")
print("<*>", end="")
for spasi_1001 in range(2 * n_1001 + 1):
    print(" ", end="")
print("|", end="")
print()

#---------Fae 3 Angka menaik (baris 1 -> N)-------
for baris_1001 in range(1, n_1001 + 1):
    print("| ", end="")
    for spasi_1001 in range(2 * (n_1001 - baris_1001)):
        print(" ", end="")
    for angka_1001 in range(baris_1001, 0, -1):
        print(angka_1001, end=" ")
    print("<*>", end="")
    for angka_1001 in range(1, baris_1001 + 1):
        print(" ", end="")
        print(angka_1001, end="")
    for spasi_1001 in range(2 * (n_1001 - baris_1001)):
        print(" ", end="")
    print(" |", end="")
    print()

# ---------- Bingkai bawah ----------
print("#", end="")
for i_1001 in range(4 * n_1001 + 5):
    print("=", end="")
print("#")