from admin import Admin

# Membuat instance Admin
admin = Admin("Salsabila", "Berliana")

# Menampilkan informasi user
admin.describe_user()

# Menampilkan privileges
admin.privileges.show_privileges()