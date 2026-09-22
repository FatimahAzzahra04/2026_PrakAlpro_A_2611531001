umur_1001 = int(input("Input umur anda: "))
sim_1001 = input("Apakah Anda Sudah Punya SIM C (y/t): ")[0]

if umur_1001  >= 17 and sim_1001 == 'y':
    print("Anda sudah dewasa dan boleh bawa motor")

if umur_1001 >= 17 and sim_1001 != 'y':
    print("Anda sudah dewasa tapi tidak boleh bawa motor")

if umur_1001 < 17 and sim_1001 != 'y' :
    print("Anda belum cukup umur bawa motor")

if umur_1001 < 17 and sim_1001 == 'y':
    print("Anda belum cukup umur punya SIM")