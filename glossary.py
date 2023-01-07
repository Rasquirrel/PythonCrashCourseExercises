glossary = {
           'print()': 'Prints a message on the terminal.',
           'str()': 'Converts an object type to string.',
           'int()': 'Converts an object type to integer.',
           'list()': 'Converts an object type to list.',
           'for()': 'This is a loop structure.'
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
