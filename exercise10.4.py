from pathlib import Path

nama = input("Siapa nama Anda? ")
Path("guest.txt").write_text(nama)