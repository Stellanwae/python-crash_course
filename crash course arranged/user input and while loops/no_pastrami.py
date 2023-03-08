sandwich_orders = ['peanut butter', 'pastrami', 'avocado', 'pastrami','apple', 'pastrami', 'banana']
finished_sandwich = []
print('Deli has ran out of pastrami')
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
for sandwich in sandwich_orders:
    finished_sandwich.append(sandwich)

print(finished_sandwich)
print('the new one')
for sandwich in finished_sandwich:
    print('Finished making your {} sandwich'.format(sandwich))
