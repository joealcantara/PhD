sandwich_orders = ['Ham Sandwich', 'BLT Sandwich', 'Pastrami Sandwich', 'Cheese and Pickle Sandwich', 
                'Bacon Sandwich', 'Pastrami Sandwich', 'Ham and Lettuce Sandwich', 'Pastrami Sandwich']
finished_sandwiches = []

print("Sorry, I am out of Pastrami")
while 'Pastrami Sandwich' in sandwich_orders:
    sandwich_orders.remove('Pastrami Sandwich')

while sandwich_orders:
    sandwich = sandwich_orders.pop()

    print("\nI'm making your " + sandwich + ".")
    finished_sandwiches.append(sandwich)

print("Here is the list of things I made:")
for sandwich in finished_sandwiches:
    print(sandwich)
