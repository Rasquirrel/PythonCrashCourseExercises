filename = 'python_learning.txt'

with open(filename) as file_object:
    # Print the contents by reading the entire file
    '''
    contents = file_object.read()
    print(contents.rstrip())
    print()
    '''
    # Print the contents by reading line by line
    '''
    for line in file_object:
        print(line.rstrip())
    '''
    # Print the contes by storing each line in a list
    lines = file_object.readlines()
    for line in lines:
        print(line.rstrip())
