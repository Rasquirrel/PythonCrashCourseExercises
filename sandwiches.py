def make_sandwich(*ingredients):
    for ingredient in ingredients:
        print('\tAdding ' + ingredient)


print('Fazer um sandwiche, por favor, insira os ingredientes que você deseja:')

make_sandwich('feijao', 'carne', 'tomate')
make_sandwich('cebolas', 'cenouras', 'calabresas')
make_sandwich('queijo', 'alface', 'bife')
