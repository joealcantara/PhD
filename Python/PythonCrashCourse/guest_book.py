filename = 'guest_book.txt'
guest = 'Blank'
while guest != '':
    guest = input("Please enter your name :")
    if guest == '':
        break
    
    print('Hello, ' + guest + '. Sign our guestbook!')
    message = (guest.title() + ' was ere.\n')

    with open(filename, 'a') as file_object:
        file_object.write(message)