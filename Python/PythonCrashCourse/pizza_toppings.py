active = True

while active == True:
    topping = input("Please enter a pizza topping: ('quit to exit') ")
    if topping != "quit":
        print(topping)
    else:
        active = False

    