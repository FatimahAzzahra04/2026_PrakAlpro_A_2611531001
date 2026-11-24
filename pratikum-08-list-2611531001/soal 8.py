number_of_rows = 4
seats_per_row = 5

seats = []
for r in range(number_of_rows):
    row = []
    for s in range(seats_per_row):
        row.append(".")
    seats.append(row)

while True:
    # Tampilkan denah
    for r in range(number_of_rows):
        print(f"Row {r + 1}: " + " ".join(seats[r]))

    row_no = int(input("Row (0 to stop): "))
    if row_no == 0:
        break

    seat_no = int(input("Seat: "))

    if row_no < 1 or row_no > number_of_rows or seat_no < 1 or seat_no > seats_per_row:
        print("Invalid seat.")
    elif seats[row_no - 1][seat_no - 1] == "X":
        print("Seat already taken.")
    else:
        seats[row_no - 1][seat_no - 1] = "X"
        print("Seat booked.")

# Hitung kursi terisi
taken = 0
for r in range(number_of_rows):
    for s in range(seats_per_row):
        if seats[r][s] == "X":
            taken += 1

print(f"Seats taken: {taken}")