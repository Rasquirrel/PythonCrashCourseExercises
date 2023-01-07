favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phill': 'python'
}

friends = ['phill', 'sarah']

'''
for name in favorite_languages.keys():
    print(name.title())
    
    if name in friends:
        print('Hello ' + name.title() + '!')
        print('I know that your favorite language is: ')
        print(favorite_languages[name])
if 'erin' not in favorite_languages.keys():
    print('Erin, please, take our pool!')
'''

'''
for name in sorted(favorite_languages.keys()):
    print("Hello " + name.title() + "!\nThanks you for taking our pool.")
'''

print("The following languages ware mentioned: ")
for language in set(sorted(favorite_languages.values())):
    print(language.title())
