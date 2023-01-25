import json

name = input('What is your name? ')

file_name = 'username.json'

with open(file_name, 'w') as f_obj:
    json.dump(name, f_obj)

print('We will remember you when you came back, ' + name.title())

