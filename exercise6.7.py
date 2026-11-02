person = {
    'first_name': 'Aluna',
    'last_name': 'Nayra',
    'age': 18,
    'city': 'Bandung'
}
person2 ={
    'first_name': 'Nayyara',
    'last_name': 'Putri',
    'age': 15,
    'city': 'Yogyakarta'
}
person3 ={
    'first_name': 'Bob',
    'last_name': 'Marley',
    'age': 25,
    'city': 'Jakarta'
}

people = [person, person2, person3]
for person in people:
    print(f"First Name: {person['first_name']}")
    print(f"Last Name: {person['last_name']}")
    print(f"Age: {person['age']}")
    print(f"City: {person['city']}\n")