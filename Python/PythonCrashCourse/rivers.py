rivers = {'Nile': 'Egypt', 'Thames': "England", 'Seine': 'France'}

for k, v in rivers.items():
    print("The river " + k + " is in " + v)

for k in rivers.keys():
    print(k)

for v in rivers.values():
    print(v)