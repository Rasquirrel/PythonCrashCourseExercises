def build_profile(first, last, **user_info):
    """Builds a dictionary containing everything we knows about a user"""
    profile = {'first': first, 'last': last, 'full name': first + ' ' + last}

    for key, value in user_info.items():
        profile[key] = value
    return profile


def display_profile(user_name):
    print('Information about user: ')
    for key1, value1 in user_name.items():
        if type(value1) == int:
            print('\t' + key1.title() + ': ' + str(value1))
        else:
            print('\t' + key1.title() + ': ' + value1.title())


eu = build_profile('isac', 'araujo', age=16, location='sobral',
                   programming_language='python', likes='emilly')

display_profile(eu)
