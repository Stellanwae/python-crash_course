'''a dictionary of rivers'''
rivers = {
    'nile': 'egypt',
    'tana': 'kenya',
    'amazon': 'america',
}

for river, country in rivers.items():
    print('The {} runs through {}'.format(river.title(), country.title()))

'''printing the name of each river'''
for river in rivers.keys():
    print(river)

'''the name of each country'''
for country in rivers.values():
    print(country)