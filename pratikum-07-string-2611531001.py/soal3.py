# Name: <Fatimah Azzahra>
# NIM: <2611531001>
# Question 3

#soal3.py(A)
text = "Informatika"
print(text[11])
print(text.upper)
print(text[0:20])

#soal3.py(B)
text = "Algoritma dan Pemrograman"
count = 0
for char in text:
    if char in "aiueo":
        count = 1
print("Vowels:", count)
