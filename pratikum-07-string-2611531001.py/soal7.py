full_name = " Siti Aisyah "
nim = "2610511023"

# Username dari Soal 6 (tanpa split)
clean = full_name.strip()
space = clean.find(" ")

if space == -1:
    first = clean
else:
    first = clean[:space]

username = first.lower() + nim[-3:]

# Nama disimpan huruf kecil di variabel name
name = clean.lower()

# Angkatan dari 2 digit pertama NIM
intake = "20" + nim[:2]

width = 30
line = "=" * width

print(line)
print("STUDENT CARD".center(width))
print(line)
print("Name".ljust(10) + ": " + name.title())
print("NIM".ljust(10) + ": " + nim)
print("Username".ljust(10) + ": " + username)
print("Intake".ljust(10) + ": " + intake)
print(line)