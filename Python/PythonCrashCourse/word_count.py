def count_words(filename, word):
    """ Count the approximate number of words in a file. """
    try:
        with open(filename) as fileobject:
            contents = fileobject.read()
    except FileNotFoundError:
        pass
        # msg = ("Sorry, the file " + filename + " does not exist." )
        # print(msg)
    else:
        # Count the approximate number of words in a file.
        words = contents.split()
        word_count = words.count(word)
        print("The number of time the word " + word + " is in this text is : " + str(word_count))
        num_words = len(words)
        print("The file " + filename + " contains approximately " + 
        str(num_words) + " words.")

filenames = ['alice.txt', 'siddartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    count_words(filename, "the")