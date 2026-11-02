pet1 = {
    'animal': 'cat',
    'owner': 'nayya',
    'age': 1
}
pet2 = {
    'animal': 'fish',
    'owner': 'vela',
    'age': 2
}
pet3 = {
    'animal': 'horse',
    'owner': 'salsa',
    'age': 5
}
pets = [pet1, pet2, pet3]    
for pet in pets:
    print(f"\nanimal: {pet['animal']}")
    print(f"owner: {pet['owner']}")
    print(f"age: {pet['age']} years old")