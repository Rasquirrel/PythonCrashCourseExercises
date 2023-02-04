import json

file_name = 'favorite_number.json'

with open(file_name) as fv_j:
    favorite_number = json.load(fv_j)
menssagem = 'Eu sei seu número favorito! É ' + str(favorite_number)
print(menssagem)

