cats = 'cats.txt'
dogs = 'dogs.txt'

def read_file(filename):
    try:
        with open(filename) as f:
            content = f.read()
            print(content)
    except FileNotFoundError:
        pass

read_file(cats)