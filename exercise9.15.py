import random
import string

# Daftar angka dan huruf
lottery = list(range(10)) + list(string.ascii_uppercase[:5])

# Tiket milik kita
my_ticket = [3, 'A', 7, 'D']

# Menghitung percobaan
attempts = 0

while True:
    winning_ticket = random.sample(lottery, 4)
    attempts += 1

    if set(winning_ticket) == set(my_ticket):
        print("Congratulations! You won the lottery!")
        print("Your ticket:", my_ticket)
        print("Winning ticket:", winning_ticket)
        print("Number of attempts:", attempts)
        break