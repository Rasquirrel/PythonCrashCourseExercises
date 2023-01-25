# Este programa irá ler os arquivos cats.txt e dogs.txt e irá
# exibir seu conteúdo.

def print_content(filename):
    """This function will print the content of a file"""
    try:
        with open(filename) as file_object:
            lines = file_object.readlines()

            print('\nShowing the content of ' + filename + ':\n')
            for line in lines:
                print(line.rstrip())
    except FileNotFoundError:
        print('\nThe file ' + filename + " doesn't exist!\n")

cats = 'cats.txt'
dogs = 'dogs.txt'

print_content(cats)
print_content(dogs)

