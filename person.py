friends = {'emilly': {}}

print(friends)
print()

friends['emilly'] = {
    'first_name': 'emilly',
    'second_name': 'nascimento',
    'favorite_color1': 'yellow',
    'favorite_color2': 'pink',
    'characteristic': 'kind',
    'age': 8,
    'city': 'sobral',
    'hair': 'wavy long',
    'likes': 'play and eat candys'
}

emilly = friends['emilly']

print("My friend's first name is " + 
      emilly['first_name'].title() + '!')
print("And her first favorite color is: " +
      emilly['favorite_color1'] + '.')
print("And her second is: " +
      emilly['favorite_color2'] + '.')
print('I like the fact that she is very ' +
      emilly['characteristic'] + '.')
print('She is ' + str(emilly['age']) + '.')
print('She lives in ' + emilly['city'] + '.')
print('She has ' + emilly['hair'] + ' hair.')
print('And she likes ' + emilly['likes'] + '.')
