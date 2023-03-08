'''a message that will be printed in the shirt'''
def make_shirt(text, size):
    print('The text on your shirt is \'{}\' and it is {}'.format(text, size))

'''positional argument'''
make_shirt('Love is a verb', 'small')

'''keyword argument'''
make_shirt(text = 'Love is a verb!', size='small')