while True:
    name = input("Masukkan nama (ketik 'quit' untuk selesai): ")

    if name == "quit":
        break

    with open("guest_book.txt", "a") as file:
        file.write(name + "\n")

    print("Nama berhasil ditambahkan!")