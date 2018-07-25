requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
    print("Hold the anchovies!")

requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print('Adding Mushrooms')
if 'pepperoni' in requested_toppings:
    print('Adding Pepperoni')
if 'extra cheese' in requested_toppings:
    print('Adding Extra Cheese')

print("\nFinished making your pizza!")

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for topping in requested_toppings:
    if topping == 'green peppers':
        print("Sorry we are out of green peppers right now.")
    else:
        print("Adding " + topping + ".")

print("\nFinished making your pizza!")

requested_toppings = []

if requested_toppings:
    for topping in requested_toppings:
        print("Adding " + topping + ".")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")

available_toppings = ['mushrooms', 'olives', 'green peppers',
                        'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for topping in requested_toppings:
    if topping in available_toppings:
        print("Adding " + topping + ".")
    else:
        print("Sorry, we don't have " + topping + ".")

print("\nFinished making your pizza.")