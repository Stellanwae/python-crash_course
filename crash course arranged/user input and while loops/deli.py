sandwich_orders = ['peanut butter', 'avocado', 'apple', 'banana']
finished_sandwiches = []
for sandwich in sandwich_orders:
    print('I made your {} sandwich'.format(sandwich))
    finished_sandwiches.append(sandwich)

for sandwich in finished_sandwiches:
    print('Your {} sandwich has been made'.format(sandwich))