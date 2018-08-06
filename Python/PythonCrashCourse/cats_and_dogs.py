filenames = ["cats1.txt", "dogs.txt"]

for filename in filenames:
    try:
        with open(filename) as fileobject:
            contents = fileobject.read()
    except FileNotFoundError:
        # print(filename + " - file is missing.")
        # print("#" * 12)
        pass
    else:
        print(contents)
        print("*" * 12)
