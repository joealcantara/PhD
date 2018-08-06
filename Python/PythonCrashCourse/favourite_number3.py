import json

filename = 'favourite.json'
with open(filename, 'w') as f_obj:
    fav_num = input("What is your favourite number? ")
    json.dump(fav_num, f_obj)


