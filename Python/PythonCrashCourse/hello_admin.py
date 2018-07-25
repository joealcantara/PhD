# usernames = []
usernames = ['admin', 'joe', 'steve', 'jenny', 'liz']
if usernames:
    for name in usernames:
        if name == 'admin':
            print("Hello admin, would you like a status report?")
        else:
            print("Hello " + name + ", you are now logged in.")
else:
    print("We need to find some users.")