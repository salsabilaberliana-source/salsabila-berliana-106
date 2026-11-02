my_foods=["pizza", "burger", "sushi", "pasta", "salad"]
friend_foods=my_foods[:]
my_foods.append("ice cream")
friend_foods.append("chocolate")
print("My favorite foods are:")
for food in my_foods:
    print(f"- {food}")  
    
print("\nMy friend's favorite foods are:")
for food in friend_foods:
    print(f"- {food}")