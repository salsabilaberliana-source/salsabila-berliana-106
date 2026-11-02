favorite_numbers = {
    "Alice": [9, 7, 3],
    "Nayya": [17, 5, 12],
    "Salsa": [28, 14, 21],
    "Vela": [20, 10, 30]
}

for name, numbers in favorite_numbers.items():
    print(f"{name}'s favorite numbers are:")
    for number in numbers:
        print(f" - {number}")