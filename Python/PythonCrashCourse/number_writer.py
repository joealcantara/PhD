import json

numbers = [2, 3, 5, 7, 11, 13]

filename = 'numbers.json'
with open(filename, 'w') as fileobject:
    json.dump(numbers, fileobject)