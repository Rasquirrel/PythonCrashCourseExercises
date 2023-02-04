# This program will ask the user's name and store it in a file

nome = input('Welcome to RASQdevelopment! Please, enter your name: ')

file_name = 'guest.txt'

with open(file_name, 'w') as file_object:
    file_object.write(nome)

