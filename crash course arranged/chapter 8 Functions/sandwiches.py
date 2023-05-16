'''Accepts a list of items on a sandwich'''
def sandwiches(*ingridients):
    new_list = []
    for i in ingridients:
        new_list.append(i)
    print(new_list)

sandwiches('peanut', 'onions', 'avocado')
list = ['peanut butter', 'jam']
print(list)