sandwich_orders = ['Ham Sandwich', 'BLT Sandwich', 'Cheese and Pickle Sandwich', 'Bacon Sandwich']
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()

    print("\nI'm making your " + sandwich + ".")
    finished_sandwiches.append(sandwich)

print("Here is the list of things I made:")
for sandwich in finished_sandwiches:
    print(sandwich)
