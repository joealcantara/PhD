print("Give me two numbers and I'll divide them.")
print("Enter 'q' to quit")

while True:
    firstNumber = input("\n\tFirst Number : ")
    if firstNumber == 'q':
        break
    secondNumber = input("\n\tSecond Number : ")
    if secondNumber == 'q':
        break
    try:
        answer = int(firstNumber) / int(secondNumber)
    except ZeroDivisionError:
        print("You can't divide by zero!")
    else:
        print(answer)