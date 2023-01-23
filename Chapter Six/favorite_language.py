from collections import OrderedDict
'''
favorite_languages = {
          'jen': ['python', 'ruby'],
          'sarah': ['c'],
          'edward': ['ruby', 'go'],
          'phil': ['python', 'haskell']
          }

for name, languages in favorite_languages.items():
    print("\n" + name.title() + "'s favorite languages are: ")
    for language in languages:
        print("\t" + language.title())
'''

favorite_languages = OrderedDict()

favorite_languages['jen'] = 'python'
favorite_languages['isac'] = 'ruby'
favorite_languages['carl'] = 'c'

for name, language in favorite_languages.items():
    print('\t' + name.title() + ': ' + language.title())
