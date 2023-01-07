glossary = {
           'print()': 'Prints a message on the terminal.',
           'str()': 'Converts an object type to string.',
           'int()': 'Converts an object type to integer.',
           'list()': 'Converts an object type to list.',
           'for()': 'This is a loop structure.',
           'set()': 'Converts an object type to set.',
           'keys()': 'Creates a list with the keys from an dictionary.',
           'values()': 'Creates a list with the values from an dictionary.',
           'items()': 'Creates a list with the keys and values from an dictionary.'
           }
'''
print('"print()" : ' + glossary['print()'])
print('"str()" : ' + glossary['str()'])
print('"int()" : ' + glossary['int()'])
print('"list()" : ' + glossary['list()'])
print('"for()" : ' + glossary['for()'])
'''

for method, definition in glossary.items():
    print("\n" + method + ": " + definition)
