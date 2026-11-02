items=['laptop', 'keyboard', 'mouse', 'printer', 'smartphone']
print("the first three items in the list are:")
print(items[:3])

middle_index = len(items)//2
print("\nThree items from the middle index and slice 3 items around it are:")
print(items[middle_index - 1: middle_index + 2])

print("\nThe last three items in the list are:")
print(items[-3:])