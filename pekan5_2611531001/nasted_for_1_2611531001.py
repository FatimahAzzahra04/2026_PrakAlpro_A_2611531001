batas_1001 =int(input("Masukkan nilai batas: "))
for line_1001 in range(1, batas_1001+1):
    for j in range(1, (-1 * line_1001 + batas_1001) + 1):
        print("." \
        "1", end= "")
    print(line_1001)