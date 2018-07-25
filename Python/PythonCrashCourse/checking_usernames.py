current_users = ['admin', 'joe', 'steve', 'eloise', 'jenny']
new_users = ['alice', 'STEVE', 'bob', 'charles', 'eloise']

for user in new_users:
    if user.lower() in current_users:
        print("This username: " + user + " is not available.")
    else: 
        print("This username: " + user + " is available.")