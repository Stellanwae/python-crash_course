def make_album(name, album_title ):
    album = {'name': name, 'album_title': album_title}

    return album

'''making three dictionaries'''
travelling_boots = make_album('forgot name', 'Today is your wedding day')
pepo_zivume = make_album('jabali chorale', 'hata pepo zivume')
peasall_sisters = make_album('peasall sisters', 'further along')

print(travelling_boots)
print(pepo_zivume)
print(peasall_sisters)

def make_album(name, album_title, number_of_songs=None ):
    if number_of_songs:
        album = {'name': name, 'album_title': album_title, 'number of songs': number_of_songs}
    else:
        album = {'name': name, 'album_title': album_title}

    return album

travelling_boots = make_album('forgot name', 'Today is your wedding day', 3)
pepo_zivume = make_album('jabali chorale', 'hata pepo zivume', 8)
peasall_sisters = make_album('peasall sisters', 'further along')

print(travelling_boots)
print(pepo_zivume)
print(peasall_sisters)