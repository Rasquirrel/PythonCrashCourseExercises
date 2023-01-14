def build_person(first_name, last_name, middle_name='', age='', city=''):
    person = {'first': first_name,
              'last': last_name
            }
    if middle_name:
        person['middle'] = middle_name
    
    if age:
        person['age'] = age

    if city:
        person['city'] = city

    return person

# musician = build_person('jimi', 'hendrix')

# print(musician)

girl = build_person('emilly', 'nascimento', 'do', 8, 'sobral')

print(girl)
