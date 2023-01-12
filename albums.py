def make_album(title, artist, n_tracks=''):
    album = {
        'title': title.title(),
        'artist': artist.title()
    }

    if n_tracks:
        album['n_tracks'] = n_tracks

    return album

album1 = make_album('pop', 'michael')
album2 = make_album('eletro', 'psyqui')
album3 = make_album('chipheat', 'ex-lyd', 13)


print(album1)

for key, value in album3.items():
    print(key.title() + ": " + str(value).title())
