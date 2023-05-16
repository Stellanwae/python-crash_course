cats = 'cats.txt'
dogs = 'dogs.txt'

def read_file(filename):
    try:
        with open(filename) as f:
            content = f.read()
            print(content)
    except FileNotFoundError:
        print(f'Sorry, {filename} does not exist')

read_file(cats)