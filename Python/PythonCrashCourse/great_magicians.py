magicians = ['Bob', 'Joe', 'Carly', 'Uma']
greater_magicians = []

def great_magicians(magician, greater_magicians):
    """
    Takes the name of a magician and adds the title great to it.
    """
    while magicians:
        current_magician = magician.pop()    
        current_magician = "The Great " + current_magician
        greater_magicians.append(current_magician)
    
def show_magicians(list_of_magicians):
    """
    Takes a list and prints out each element of the list.
    """
    for magician in list_of_magicians:
        print(magician)


great_magicians(magicians, greater_magicians)
show_magicians(greater_magicians)
