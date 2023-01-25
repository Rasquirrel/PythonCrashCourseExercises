import json

file_name = 'numbers.json'

numbers = [7, 8, 9, 11, 15, 19]

with open(file_name, 'w') as f_obj:
    json.dump(numbers, f_obj)

