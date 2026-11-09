import json

filename = "user_info.json"

username = input("What is your name? ")
favorite_color = input("What is your favorite color? ")
age = input("How old are you? ")

user_info = {
    "username": username,
    "favorite_color": favorite_color,
    "age": age
}

with open(filename, "w") as f:
    json.dump(user_info, f)

with open(filename) as f:
    user_info = json.load(f)

print("\nHere's what I know about you:")
print(f"Username: {user_info['username']}")
print(f"Favorite color: {user_info['favorite_color']}")
print(f"Age: {user_info['age']}")