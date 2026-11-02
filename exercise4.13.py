buffet_foods=["nasi goreng", "sate ayam", "bakso", "soto", "ayam goreng"]
print("Original menu:")
for food in buffet_foods:
 print(food)

print("\nModified menu:")
buffet_foods[0] = "nasi padang"
for food in buffet_foods:
 print(food)

