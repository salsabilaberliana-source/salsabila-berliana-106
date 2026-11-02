cubes = [value**3 for value in range(1, 11)]

print("The first three items in the list are:")
print(cubes[:3])

middle_index = len(cubes) // 2
print("\nThree items from the middle of the list are:")
print(cubes[middle_index - 1: middle_index + 2])

print("\nThe last three items in the list are:")
print(cubes[-3:])
