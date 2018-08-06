with open('learning_python.txt') as file_object:
    contents = file_object.read()
    print(contents)
    print("*" * 8)

with open('learning_python.txt') as file_object:
    for line in file_object:
        print(line.rstrip())

with open('learning_python.txt') as file_object:
    lines = file_object.readlines()

print("*" * 8)
for line in lines:
    print(line.rstrip())

print("*" * 8)
for line in lines:
    newline = line.replace("Python", "C")
    print(newline.rstrip())