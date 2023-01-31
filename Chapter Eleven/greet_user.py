import json

file_name = 'username.json'

with open(file_name) as f_obj:
    name = json.load(f_obj)
    print('Welcome back ' + name.title() + '.')

