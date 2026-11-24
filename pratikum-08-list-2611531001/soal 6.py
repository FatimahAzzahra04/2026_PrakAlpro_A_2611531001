LAST_DIGIT = 1  # change to the last digit of your NIM
daily_limit = 30000 + LAST_DIGIT * 1000
expenses = []
# Write your code bellow
for i in range(1,8):
    expenses.append(int(input(f"Day {i}: ")))

# Hitung total, hari tertinggi, dan hari di atas batas (tanpa sum/max/min)
total = 0
highest_day = 1
highest_value = expenses[0]
days_above = 0

for i in range(7):
    total += expenses[i]
    if expenses[i] > highest_value:  
        highest_value = expenses[i]
        highest_day = i + 1
    if expenses[i] > daily_limit:
        days_above += 1

average = total / 7
print("Daily limit:" ,daily_limit )
print("Total:", total)
print("Average:",round(average,2 ))
print(f"Highest: day {highest_day} ({highest_value})")
print("Days above limit:", days_above)