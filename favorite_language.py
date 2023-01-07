favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phill': 'python'
}

friends = ['phill', 'sarah']

for name in favorite_languages:
    print(name)
    if name in friends:
        print('Hello ' + name + '!')
        print('I know that your favorite language is: ')
        print(favorite_languages[name])

