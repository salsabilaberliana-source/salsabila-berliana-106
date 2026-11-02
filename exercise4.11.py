my_pizzas=["pepperoni", "margherita", "hawaiian", "bbq chicken", "veggie"]
friend_pizzas=my_pizzas[:]
my_pizzas.append("supreme")
friend_pizzas.append("meat lovers")
print("My favorite pizzas are:")
for pizza in my_pizzas:
    print(f"- {pizza}")
print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(f"- {pizza}")
