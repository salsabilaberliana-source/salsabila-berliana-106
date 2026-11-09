class User:
    def __init__(self, first_name, last_name, age, city, occupation):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city
        self.occupation = occupation

    def describe_user(self):
        print(f"First name: {self.first_name}")
        print(f"Last name: {self.last_name}")
        print(f"Age: {self.age}")
        print(f"City: {self.city}")
        print(f"Occupation: {self.occupation}")

    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}!")
        print("Welcome back!")


# Membuat beberapa instance pengguna
user1 = User("Meisha", "Davela", 18, "Mojokerto", "Mahasiswa")
user2 = User("Nayyara", "Najma", 18, "Malang", "Mahasiswa")
user3 = User("Fathia", "Carissa", 18, "Yogyakarta", "Mahasiswa")

# Menampilkan informasi dan sapaan setiap pengguna
user1.describe_user()
user1.greet_user()
print()

user2.describe_user()
user2.greet_user()
print()

user3.describe_user()
user3.greet_user()