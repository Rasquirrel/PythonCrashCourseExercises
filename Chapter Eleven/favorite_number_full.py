import json

file_name = 'favorite_number.json'

def get_fav_number():
    favorite_number = input('Qual é o seu número favorito? ')
    favorite_number = int(favorite_number)
    with open(file_name, 'w') as f_obj:
         json.dump(favorite_number, f_obj)
     print('Seu número foi armazenado no arquivo ' + file_name)


def show_number():
    menssagem = 'Eu sei seu número favorito! É ' + str(favorite_number)

def get_file(file_name):
    try:
        with open(file_name) as f_obj:
            favorite_number = json.load(f_obj)
    except FileNotFoundError:
        get_fav_number() 
    else:
        show_number()

get_file(file_name)

