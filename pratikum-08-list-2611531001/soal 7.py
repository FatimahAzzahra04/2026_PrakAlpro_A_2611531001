menus = ["Nasi Goreng", "Mie Ayam", "Soto"]
number_of_days = 3
sales = []

for day in range(1, 4):
    row = []
    for m in menus:
        row.append(int(input(f"Day {day}, {m}: ")))
    sales.append(row)

# Total per hari
print("Total per day:")
for d in range(3):
    t = 0
    for qty in sales[d]:
        t += qty
    print(f"Day {d + 1}: {t}")

# Total per menu
menu_totals = []
for j in range(3):
    t = 0
    for d in range(3):
        t += sales[d][j]
    menu_totals.append((menus[j], t))
print("Total per menu:", menu_totals)

# Menu terlaris (jika sama, pilih yang muncul lebih dulu)
best_name, best_total = menu_totals[0]
for name, total in menu_totals:
    if total > best_total:  
        best_name = name
        best_total = total
print(f"Best seller: {best_name} ({best_total})")