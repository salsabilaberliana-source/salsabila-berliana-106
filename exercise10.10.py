filenames = ["text1.txt", "text2.txt", "text3.txt"]

for filename in filenames:
    try:
        with open(filename, "r", encoding="utf-8") as file:
            contents = file.read()

            jumlah = contents.lower().count("the")

            print("File:", filename)
            print("Jumlah kata 'the':", jumlah)
            print()

    except FileNotFoundError:
        print("File", filename, "tidak ditemukan.")