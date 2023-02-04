import json

file_name = 'username.json'

try:
    with open(file_name) as f_obj:
        name = json.load(f_obj)
except FileNotFoundError:
    name = input('What is your name? ')
    with open(file_name, 'w') as f_obj:
        json.dump(name, f_obj)
        print('We will rember you when you came back ' + name.title())
else:
    print('Welcome back ' + name.title() + '!')

