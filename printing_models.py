def print_models(unprinted_list, completed_list):
    """Simulate printing each design, until none are left"""
    while unprinted_list:
        current_design = unprinted_list.pop()
        print('Printing model: ' + current_design)

        completed_list.append(current_design)


def show_completed_models(completed_list):
    print('\nThe following models have been printed: ')
    for completed_model in completed_list:
        print(completed_model)


unprinted_models = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_models, completed_models)
show_completed_models(completed_models)
