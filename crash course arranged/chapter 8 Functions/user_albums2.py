def make_album(artist='', title=''):
    while True:
        artist = input('What is the name of the artist?')
        title = input('What is the title of the album?')
        break
    new_dictionary = {'name': artist, 'title': title}
    print(new_dictionary)
        

make_album()