import json

def favourite_number():
    filename = 'favnum.txt'
    fav_number = int(input('What is your favourite number?'))
    with open(filename, 'w') as f:
        json.dump(fav_number, f)

def message():
    filename = 'favnum.txt'
    with open(filename) as f:
        number = f.read()
    print(f"I know your favourite number! It's {number}")