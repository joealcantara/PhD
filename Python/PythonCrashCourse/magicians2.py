def show_magicians(list_of_magicians):
    """
    Takes a list and prints out each element of the list.
    """
    for magician in list_of_magicians:
        print(magician.title())


magicians = ['Bob', 'Joe', 'Carly', 'Uma']

show_magicians(magicians)
