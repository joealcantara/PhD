def greet_user():
    """Display a simple greeting"""
    print("Hello!")

def greet_user2(username):
    """Display a simple greeting taking in an argument"""
    print("Hello, " + username.title() + "!")

greet_user()
greet_user2('bob')