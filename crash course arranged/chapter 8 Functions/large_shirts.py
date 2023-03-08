'''a message that will be printed in the shirt'''
def make_shirt(text='I love python', size='large'):
    print('The text on your shirt is \'{}\' and it is {}'.format(text, size))

'''printing with the default values'''
make_shirt()

'''making a medium shirt'''
make_shirt(size='medium')

'''a shirt of any size and different message'''
make_shirt(size='small', text='Charmed by Darkness by Roger Morneau')