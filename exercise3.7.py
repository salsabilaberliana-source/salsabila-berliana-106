guests = ["Vela", "Nayya", "Djilva", "Rara", "Puyes", "Mala", "Aira"]
print("unfortunately, the new table will not arrive on time")
print("I can only invite two guests for dinner.")

#remove guests untill only two remain
while len(guests) > 2:
    removed_guest = guests.pop()
    print(f"Sorry {removed_guest}, I can't invite you to dinner.")

#send invitation messages to the remaining guests
print("\nInvitation messages to the remaining guests:")
for guest in guests:
    print(f"Hello {guest}, you are still invited to dinner at my place.")
    
#delete the remaining guests
del guests[0]
del guests[0]


print(guests)