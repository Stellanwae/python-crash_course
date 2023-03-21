def make_album(name='', album ='', number_of_songs=None):
    album = {}
    while True:
        print('Write details about your fav artist ')
        print('You may enter q to quit')
        name = input('Artist name: ')
        if name == 'q':
            break
        album = input('The album: ')
        number_of_songs = input('Number of songs: ')
        if number_of_songs:
            album = {'name': name, 'album': album, 'number of songs': number_of_songs}
            break
        else:
            album = {'name': name, 'album': album}
            break
    print(album)

make_album()