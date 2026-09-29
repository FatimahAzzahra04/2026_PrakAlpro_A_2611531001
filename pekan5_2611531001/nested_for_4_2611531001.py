tinggi_1001 = int(input("Masukkan tinggi pola (bilangan genap, misal 10): "))

if tinggi_1001 % 2 !=0:
    print("Tinggi harus bilangan genap!")
else:
    a_1001 = tinggi_1001
    c_1001 = a_1001
    lebar_1001 = (2 * tinggi_1001) - 2

    for i_1001 in range(1, tinggi_1001 + 1):
        b_1001 = c_1001 + 1

        for j_1001 in range(1, lebar_1001 + 1):

            #Baris atas dan bawah
            if i_1001 == 1 or i_1001 == tinggi_1001:
                if j_1001 == 1 or j_1001 == lebar_1001:
                    print("#", end="")
                else:
                    print("=", end="")

            #Baris isi
            else:
                if j_1001 == 1 or  j_1001 == lebar_1001:
                    print("|", end="")
                else:
                    if j_1001 == c_1001:
                        print("<", end="")
                    elif j_1001 == b_1001:
                        print(">", end="")
                    elif j_1001 == (lebar_1001 - c_1001):
                        print("<", end="")
                    elif j_1001 == (lebar_1001 - c_1001 + 1):
                        print(">", end="")
                    elif j_1001 > b_1001 and j_1001< (lebar_1001 - c_1001):
                        print(".", end="")
                    else:
                        print(" ", end="")
        print()

        # Logika asli Java
        a_1001 -= 2

        if a_1001 <= 0:
            c_1001 = (-a_1001) +2
        else:
            c_1001 = a_1001