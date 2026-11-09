class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"Restaurant: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, number):
        self.number_served += number


# Membuat instance restaurant
restaurant = Restaurant("Seafood 99", "Seafood")

# Menampilkan jumlah pelanggan
print("Number served:", restaurant.number_served)

# Mengubah jumlah pelanggan
restaurant.number_served = 25
print("Number served:", restaurant.number_served)

# Menggunakan method set_number_served()
restaurant.set_number_served(50)
print("After set_number_served:", restaurant.number_served)

# Menggunakan method increment_number_served()
restaurant.increment_number_served(10)
print("After increment_number_served:", restaurant.number_served)