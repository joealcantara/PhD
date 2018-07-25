pizzas = ['Pepperoni', 'Farmhouse', 'Meat Feast']
for pizza in pizzas:
    print("I like " + pizza + " pizzas. They're the best!")
    # print("I like", pizza, "pizzas. They're the best!")

print("I really love pizza.")

friend_pizzas = pizzas[:]

print(pizzas)
print(friend_pizzas)

pizzas.append('Hawaiian')
friend_pizzas.append('Vegetarian')

print("My favourite pizza's are:")
for pizza in pizzas:
    print(pizza)
print("My friend's favourite pizza's are:")
for pizza in friend_pizzas:
    print(pizza)