print("Addition program. \n")
active = True
while active == True:
    num1 = input("Please enter a number : ")
    num2 = input("Please enter another number: ")

    try:
        num1 = int(num1)
        num2 = int(num2)
    except ValueError:
        print("You didn't enter a number")
    else:
        answer = num1 + num2
        print("\tThe answer is : " + str(answer))

    response = input("Do you want to continue? (yes / no) ")
    if response.lower == 'yes':
        active == True
    else:
        break