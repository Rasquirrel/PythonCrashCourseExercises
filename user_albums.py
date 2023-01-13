def make_album(title, artist, n_tracks=''):
    album = {
        'title': title.title(),
        'artist': artist.title()
    }
    return album

print('Welcome to the music library app!')
print('Enter "quit" any moment when you choose to leaves.')

while True:
    artist = input('What is the name of the artist? \n')
    if artist == 'quit': break
    album = input('\nWhat is the title of the album? \n')
    if album == 'quit': break

    album1 = make_album(album, artist)

    print("Here is the album:")
    for  title, artist in album1.items():
        print("\t" + title.title() + ": " + artist.title() + ";")
