class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


# Membuat instance User
user = User("Salsabila", "Berliana")

# Menambah login attempts beberapa kali
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()

# Menampilkan jumlah login attempts
print("Login attempts:", user.login_attempts)

# Mereset login attempts
user.reset_login_attempts()

# Menampilkan kembali jumlah login attempts
print("After reset:", user.login_attempts)