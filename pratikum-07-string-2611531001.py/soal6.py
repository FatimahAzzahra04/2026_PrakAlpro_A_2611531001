# Name: <Fatimah Azzahra>
# NIM: <2611531001>
# Question 5

#soal6.py
first_name = " muhammad"
last_name = "rafi "
full_name = first_name.strip() + " " + last_name.strip()
print(full_name)
print(full_name.title())

# Build the username: first name in lowercase + last 3 digits of the NIM.
# Do not use split().
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