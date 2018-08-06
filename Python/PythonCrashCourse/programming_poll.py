filename = 'response.txt'
with open(filename, 'w') as file_object:
    file_object.write("Reasons why:\n")

active = True
while active != False:
    response = input("Why do you like programming?")

    with open(filename, 'a') as file_object:
        file_object.write(response + "\n")

    willContinue = input ("Would you like to continue? (yes / no) :")
    if willContinue.lower() == 'yes':
        active = True
    else:
        active = False