filenames = ["cats.txt", "dogs.txt"]

for filename in filenames:
    try:
        with open(filename, "r") as file:
            contents = file.read()
            print(contents)

    except FileNotFoundError:
        print("Maaf, file " + filename + " tidak ditemukan.")