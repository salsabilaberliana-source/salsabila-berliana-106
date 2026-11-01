mountain = ["Merbabu", "Rinjani", "Lawu", "Bromo", "Semeru"]
print("First mountain:")
print(mountain[0])

mountain[0] = "Sumbing"
print("\nAfter changing an element:")
print(mountain)

mountain.append('Sindoro')
print("\nAfter append():")
print(mountain)

mountain.insert(0, 'Jaya Wijaya')
print("\nAfter insert():")
print(mountain)

del mountain[3]
print("\nAfter del():")
print(mountain)

popped_mountain = mountain.pop()
print("\nAfter pop():")
print(mountain)
print(f"removed mountain: {popped_mountain}")

mountain.remove('Bromo')
print("\nAfter remove():")
print(mountain)

mountain.sort()
print("\nAfter sort():")
print(mountain)

mountain.sort(reverse=True)
print("\nAfter sort(reverse=True):")
print(mountain)

print("\nUsing sorted():")
print(sorted(mountain))

mountain.reverse()
print("\nAfter reverse():")
print(mountain)

print("\nNumber of mountains:")
print(len(mountain))
