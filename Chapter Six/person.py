emilly = {
    'first': 'emilly',
    'last': 'do nascimento',
    'color': 'yellow',
    'likes': 'play and eat candys',
    'location': 'sobral',
    'age': 8
}

isac = {
    'first': 'josé',
    'last': 'isac',
    'color': 'gray',
    'likes': 'study python and play with Emilly',
    'location': 'sobral',
    'age': 16
}

sales = {
    'first': 'gabriel',
    'last': 'sales',
    'color': 'black',
    'likes': 'listen to music and be with his girlfriend',
    'location': 'aracatiaçu',
    'age': 17
}

friends = [emilly, isac, sales]

print("These are some of my friends: ")

for friend in friends:
    full_name = friend['first'] + " " + friend['last']
    color = friend['color']
    likes = friend['likes']
    location = friend['location']
    age = friend['age']

    print("\tFull name: " + full_name.title() + ";")
    print("\tFavorite color: " + color + ";")
    print("\tLikes: " + likes + ";")
    print("\tLocation: " + location.title() + ";")
    print("\tAge: " + str(age) + ".\n")
