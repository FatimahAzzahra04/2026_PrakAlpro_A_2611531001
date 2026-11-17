# Name: <Fatimah Azzahra>
# NIM: <2611531001>
# Question 4

#soal4.py
phone = "08123456789"
masked = phone[:4] + "*" * 4 + phone[-4:]
print(masked)

phone = "081234567890"
masked = phone [:4] + "*" *(len(phone) - 7) + phone[-3:]
print(masked)

phone = "08123456789"
masked = phone [:4] + "*" *(len(phone) - 7) + phone[-3:]
print(masked)

phone = "0812345678"
masked = phone [:4] + "*" *(len(phone) - 7) + phone[-3:]
print(masked)

phone = "082611531001"
masked = phone [:4] + "*" *(len(phone) - 7) + phone[-3:]
print(masked)

