pet1 = {
    'animal': 'cat',
    'owner': 'nayya',
}
pet2 = {
    'animal': 'fish',
    'owner': 'vela',
}
pet3 = {
    'animal': 'horse',
    'owner': 'salsa',
}
pets = [pet1, pet2, pet3]

for pet in pets:
    print(f"\nanimal: {pet['animal']}")
    print(f"owner: {pet['owner']}")