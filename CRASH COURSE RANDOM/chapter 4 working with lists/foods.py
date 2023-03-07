'''copying a list'''
my_foods = ['pizza', 'falafel', 'carrot cake']
friends_food = my_foods[:]
print('My friends fav foods are:')
print(friends_food)

'''appending to see if original is not tampered'''
my_foods.append('cannoli')
friends_food.append('icce cream')

print('My fav foods are:')
print(my_foods)

print('My friend\'s fav foods are:')
print(friends_food)
