# Reading the entire file
with open('learning_python.txt') as file_object:
    contents = file_object.read()

print(contents)

# Reading line by line into a list
with open('learning_python.txt') as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())