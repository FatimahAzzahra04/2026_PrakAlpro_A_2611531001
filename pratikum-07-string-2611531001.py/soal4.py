# Name: <Fatimah Azzahra>
# NIM: <2611531001>
# Question 4

#soal4.py
phone = "08123456789"
masked = phone[:4] + "*" * 4 + phone[-4:]
print(masked)

#mengubah program pertama menjadi 3 digit belakang yang ditampilkan
phone = "08123456789"
masked = phone [:4] + "*" *4 + phone[-3:]
print(masked)

#tabel nomor 1 
phone = "081234567890"
masked = phone [:4] + "*" *5 + phone[-3:]
print(masked)

#tabel nomor 2
phone = "08123456789"
masked = phone [:4] + "*" *4 + phone[-3:]
print(masked)

#tabel nomor 3
phone = "0812345678"
masked = phone [:4] + "*" *3 + phone[-3:]
print(masked)

#tabel nomor 4
phone = "082611531001"
masked = phone [:4] + "*" *5 + phone[-3:]
print(masked)

