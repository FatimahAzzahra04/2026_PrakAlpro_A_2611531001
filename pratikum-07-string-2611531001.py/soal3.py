# Name: <Fatimah Azzahra>
# NIM: <2611531001>
# Question 3

#soal3.py(A)
text = "Informatika"
print(text[10])
print (text.upper())
print(text[0:20])

#soal3.py(B)
text = "Algoritma dan Pemrograman"
count = 0
for char in text:
    if char in "AIUEOaiueo":
        count = count + 1
print("Vowels:", count)

text = "Fatimah Azzahra"
count = 0
for char in text:
    if char in "AIUEOaiueo":
        count =count + 1
print("Vowels:", count)