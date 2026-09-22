umur_1001 = int(input("Input umur anda: "))
sim_1001 = input("Apakah Anda Sudah Punya SIM C: ")[0]

if umur_1001 >= 17 and sim_1001 == 'y':
    print("Anda sudah dewasa dan boleh bawa motor")
elif umur_1001 >= 17 and sim_1001 != 'y':
     print("Anda sudah dewasa tetapi tidak boleh bawa motor")
elif umur_1001 < 17 and sim_1001 =='y':
     print("Anda belum cukup umur punya SIM")
else:
     print("Anda belum cukup umur dan tidak boleh bawa motor")
print("Program Selesai")