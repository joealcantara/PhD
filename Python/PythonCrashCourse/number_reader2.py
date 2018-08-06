import json

filename = 'favourite.json'

with open(filename) as f_obj:
    fav_num = json.load(f_obj)
    print("Your favourite number is " + str(fav_num) + ".")