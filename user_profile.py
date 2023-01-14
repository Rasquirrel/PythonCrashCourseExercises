def build_profile(first, last, **user_info):
    """Builds a dictionary containing everything we knows about a user"""
    profile = {'first': first, 'last': last, 'full name': first + ' ' + last}

    for key, value in user_info.items():
        profile[key] = value
    return profile


user = build_profile('isac', 'araujo', age=16, country='Brazil')

print('Information about user: ')
for key1, value1 in user.items():
    if type(value1) == int:
        print('\t' + key1.title() + ': ' + str(value1))
    else:
        print('\t' + key1.title() + ': ' + value1.title())
