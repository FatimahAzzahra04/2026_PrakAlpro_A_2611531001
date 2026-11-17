# Name: <Fatimah Azzahra>
# NIM: <2611531001>
# Question 6

#soal6.py
first_name = " muhammad"
last_name = "rafi "
full_name = first_name.strip() + " " + last_name.strip()
print(full_name)
print(full_name.title())

#soal tabel nomor 1
full_name = " Siti Aisyah "
nim = "2610511023"

clean = full_name.strip()
space = clean.find(" ")

if space == -1:
    first = clean
else:
    first = clean[:space]

username = first.lower() + nim[-3:]
print(username)

#soal tabel nomor 2
full_name = "Muhammad Rafi Pratama"
nim = "2610511045"

clean = full_name.strip()
space = clean.find(" ")

if space == -1:
    first = clean
else:
    first = clean[:space]

username = first.lower() + nim[-3:]
print(username)

#soal tabel nomor 3
full_name = "Kartika"
nim = "2610511007"

clean = full_name.strip()
space = clean.find(" ")

if space == -1:
    first = clean
else:
    first = clean[:space]

username = first.lower() + nim[-3:]
print(username)

#soal tabel nomor 4
full_name = "Fatimah Azzahra"
nim = "2611531001"

clean = full_name.strip()
space = clean.find(" ")

if space == -1:
    first = clean
else:
    first = clean[:space]

username = first.lower() + nim[-3:]
print(username)

#program tanpa memeriksa nilai -1
full_name = "Kartika"
nim = "2610511007"

clean = full_name.strip()
space = clean.find(" ")
first = clean[:space]

username = first.lower() + nim[-3:]
print(username)