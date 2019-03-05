def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def modulus(x, y):
    return x % y

def getNumbers():
    num1 = input('Enter the first number : ')
    num2 = input('Enter the second number : ')
    return(num1, num2)

def Menu(choice):
    if choice == 1:
        num1, num2 = getNumbers()
        num1 = int(num1)
        num2 = int(num2)
        print(num1, "+", num2, add(num1, num2))
    elif choice == 2:
        num1, num2 = getNumbers()
        num1 = int(num1)
        num2 = int(num2)
        print(num1, "-", num2, subtract(num1, num2))
    elif choice == 3:
        num1, num2 = getNumbers()
        num1 = int(num1)
        num2 = int(num2)
        print(num1, "*", num2, multiply(num1, num2))
    elif choice == 4:
        num1, num2 = getNumbers()
        num1 = int(num1)
        num2 = int(num2)
        print(num1, "/", num2, divide(num1, num2))
    elif choice == 5:
        num1, num2 = getNumbers()
        num1 = int(num1)
        num2 = int(num2)
        print(num1, "%", num2, modulus(num1, num2))
    else:
        print('Not a legal operation')
    
def MenuChoice ():
    print('Select Operation')
    print('1: Add')
    print('2: Subtract')
    print('3: Multiply')
    print('4: Divide')
    choice = input('Please enter a selection: ')
    int(choice)
    return choice