from name_function import get_formatted_name

print('Enter "q" at any moment to quit.')

while True:
    first_name = input('What is your first name? ')
    if first_name == "q":
        break;
    last_name = input('What is your last name? ')
    if last_name == "q":
        break;
    full_name = get_formatted_name(first_name, last_name)
    print('\nYour full name is ' + full_name.title())

