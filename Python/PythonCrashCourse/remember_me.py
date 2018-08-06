import json
# Load the username, if it has been stored previously.
# Otherwise, prompt for the username and store it.
def get_stored_username():
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """ Prompt user for a username """ 
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username        

def greet_user():
    """ Greet user by name """
    username = get_stored_username()
    if username:
        check = input("Is your username - " + username + " ? (y/n)")
        if check == 'y':
            print("Welcome back, " + username + "!")
        elif check == 'n':
            get_new_username()
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username + "!")

greet_user()