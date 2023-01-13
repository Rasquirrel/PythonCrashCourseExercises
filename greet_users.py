def greet_users(names: list):
    """Prints a greeting for each name in the list"""
    for name in names:
        print("Hello, " + name.title() + "!")


usernames = ['lisa', 'v', 'sleep']

greet_users(usernames)
