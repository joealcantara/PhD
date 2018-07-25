joe = {'firstname': 'joe', 'lastname': 'alcantara', 'age': 41, 'city': 'birmingham'}
italia = {'firstname': 'italia', 'lastname': 'ricci', 'age': 37, 'city' : 'toronto'}
hailey = {'firstname': 'hailey', 'lastname': 'little', 'age': 21, 'city' : 'los angeles'}

people = [joe, italia, hailey]

for person in people:
    full_name = person['firstname'] + ' ' + person['lastname']
    print("Full Name: " + full_name)
    print("Age: " + str(person['age']))
    print("From: " + person['city'])