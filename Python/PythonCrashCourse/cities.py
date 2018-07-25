cities = {
    'london': {
        'country': 'england',
        'population': 8000000,
        'famous site': 'tower of london',
        },
    'seattle': {
        'country': 'united states',
        'population': 5000000,
        'famous site': 'space needle',
        },
    'paris': {
        'country': 'france',
        'population': 7000000,
        'famous site': 'le louvre',
        },
    }

for k, v in cities.items():
    print(k.title())
    print("Country: " + v['country'].title())
    print("Population: " + str(v['population']))
    print("Famous Site: " + v['famous site'].title())