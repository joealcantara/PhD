active = True

while active == True:
    age = input("Enter your age: ")
    if age == 'quit':
        active = False
        break
    
    age = int(age)
    if age < 3:
        price = 0
    elif age < 12:
        price = 10
    else:
        price = 15

    print("Your ticket price is $" + str(price) + ".")

print("End of program.")