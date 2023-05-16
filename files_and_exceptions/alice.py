'''Handling file not found error'''

filename = 'alice.txt'
try:
    with open(filename) as file_object:
        open_file_object = file_object.read()
        print(open_file_object)
except FileNotFoundError:
    print('Sorry, {} does not exist'.format(filename))

