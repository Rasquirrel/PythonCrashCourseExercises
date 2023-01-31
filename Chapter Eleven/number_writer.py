import json

file_name = 'numbers.json'

numbers = ['2', '3', '5', '7', '11', '13']

with open(file_name, 'w') as f_obj:
    json.dump(numbers, f_obj)

