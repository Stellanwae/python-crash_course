'''ordinal numbers end with th
except 1, 2 and 3'''

ordinal_numbers = list(range(1,10))
print(ordinal_numbers)

for num in ordinal_numbers:
    if num == 1:
        print('{}st'.format(num))
    elif num == 2:
        print('{}nd'.format(num))
    elif num == 3:
        print('{}rd'.format(num))
    else:
        print('{}th'.format(num))