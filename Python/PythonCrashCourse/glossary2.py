glossary = {'Print': 'Prints a statement',
            'if..else': 'conditional statement',
            'for' : 'A loop',
            '.append': 'a function that appends an item to a list', 
            '.sort': 'a function that sorts a list into alphabetical order.',
            '.items': 'a function that gets all keys and values from a dictionary.',
            '.keys': 'a function that gets just the keys from a dictionary.',
            '.values': 'a function that gets just the values from a dictionary.',
            '.sorted': 'a function that temporarily sorts a list',
            '.title': 'a function that takes a string and turns it into a capitalised string.'}

for k, v in glossary.items():
    print(k.title() + ": " + v)