import module_pizza
module_pizza.make_pizza(16, "pepperoni", "onion")

'''Importing specific functions'''
from module_pizza import make_pizza
make_pizza(12, 'mushrooms', 'green peppers')

'''using as to give a module an alias'''
import module_pizza as md
print('Using an alias')
md.make_pizza(12, "mushrooms", "extra cheese")

'''importing all functions in a module'''
from module_pizza import *
