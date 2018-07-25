favourite_numbers = {'Joe': [7], 'Lisa': [42, 69], 'Bob': [1, 13], 'Klay': [11, 23], 'Jenny': [12]}

for k, v in favourite_numbers.items():
    print(k + "'s favourite numbers are")
    for i in v:
        print("\t" + str(i))