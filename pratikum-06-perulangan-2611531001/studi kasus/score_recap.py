PASS_SCORE = 65
total   = 0
passed  = 0
lowest  = 100

n = int(input("Number of students: "))
while n < 1:
    print("Invalid student count !")
    n = int(input("Number of students: "))

for s in range (1, n+1):
    print("Student",s)
    score = (int(input("Enter score: ")))

    while score < 0 or score > 100:
        print("Invalid score!")
        score = (int(input("Enter score: ")))
    
    total += score

    if score >= PASS_SCORE:
        passed += 1
    if score < lowest:
        lowest = score

average = total / n

print ("Total: ", total)
print ("Average: ", round(average,2))
print ("Passed student: ", passed)
print ("Lowest Score: ", lowest )

