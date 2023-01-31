import json

file_name = 'favorite_number.json'

fav_number = input('Qual é seu número favorito? ')
fav_number = int(fav_number)

with open(file_name, 'w') as fv_j:
    json.dump(fav_number, fv_j)
    print('O número foi armazenado no arquivo ' + file_name)

