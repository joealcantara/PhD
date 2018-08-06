import json

filename = 'numbers.json'
with open(filename) as fileobject:
    numbers = json.load(fileobject)

print(numbers)