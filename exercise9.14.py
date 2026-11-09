import random
import string

# Membuat daftar angka dan huruf
lottery = list(range(10)) + list(string.ascii_uppercase[:5])

print("Lottery items:")
print(lottery)

# Memilih 4 angka atau huruf secara acak
winning_ticket = random.sample(lottery, 4)

print("\nWinning ticket:")
print(winning_ticket)

print("\nAny ticket matching these 4 numbers or letters wins a prize!")