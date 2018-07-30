def make_pizza(*toppings):
    """ Print the list of toppings have been requested """
    print(toppings)

def make_pizza2(size, *toppings):
    """ Summarize the pizza we are about to make """
    print("\nMaking a " + str(size) +
        "-inch pizza with the following toppings:  ")
    for topping in toppings:
        print(" - " + topping)

make_pizza('Pepperoni')
make_pizza('Mushrooms', 'Green Peppers', 'Extra Cheese')

make_pizza2(16, 'Pepperoni')
make_pizza2(12, 'Mushrooms', 'Green Peppers', 'Extra Cheese')