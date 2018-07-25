favourite_places = {'joe': ['London', 'Chicago', 'Seattle'],
                'fred': ['Tokyo', 'London', 'Paris'],
                'donald': ['Moscow', 'Washington', 'Wonderland']}

for k, v in favourite_places.items():
    print(k.title())
    for item in v:
        print("\t" + item)