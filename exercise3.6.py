guests = ["Vela", "Nayya", "Djilva", "Rara"]
print("initial guest list:")

for guest in guests:
    print("Hello", guest, ",I would like to invite you to dinner at my place.")
print("\nI found a bigger dinner table, so I can invite more guests.")

#Add a new guest to the beginning of the list
guests.insert(0, "Puyes")

#Add a new guest to the middle of the list
guests.insert(2, "Mala")

#Add a new guest to the end of the list
guests.append("Aira")

#print the new invitation message
print("\nNew invitation messages:")
for guest in guests:
    print("Hello", guest, ",I would like to invite you to dinner at my place.")