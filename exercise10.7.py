while True:
    try:
        angka1 = int(input("Masukkan angka pertama: "))
        angka2 = int(input("Masukkan angka kedua: "))

        hasil = angka1 + angka2

        print("Hasil penjumlahan:", hasil)

    except ValueError:
        print("Error! Masukkan angka yang benar.")

    ulang = input("Apakah ingin menghitung lagi? (ya/tidak): ")

    if ulang.lower() == "tidak":
        break

print("Program selesai.")