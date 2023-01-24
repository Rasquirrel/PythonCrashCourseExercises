filename = 'python_learning.txt'

with open(filename) as file_object:
    content = file_object.read()
    print(content.replace('Python', 'Ruby').rstrip())
