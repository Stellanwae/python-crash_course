#looping through an entire list
shop_list = ["pampers", "fruits", "cabbage", "porridge flour"]
for i in shop_list:
    print(i)
for i in shop_list:
    print("{} is an item in the shopping list".format(i.title()))
print("That's an interestig item in the list")

foods = ["minji", "proya", "lentils", "kienyeji"]
for food in foods:
    print("{} is a favourite food". format(food))
print("\nThis is food is so delicious")

'''Numerical Lists'''
print("\n")
for value in range(1,5):
    print(value)

'''converting the results of a range into a list
using the list() function'''
numbers = list(range(1, 6))
print(numbers)

'''printing even numbers'''
even_numbers = list(range(2, 11, 2))
print(even_numbers)
'''Adding squares in a list'''
squares = []
for i in range(1, 11):
    square = i**2
    squares.append(square)
print(squares)
print(min(squares))
print(max(squares))
print(sum(squares))
'''List comprehensions
this does in one line, what other for loops
do in three'''
#printing 1 to 20 using list comprehensions
double = [value for value in range(1,21)]
print(double)
squares = [i**2 for i in range(1,21)]
print(squares)

'''use for loop to print number 1 to 20'''
numero = [num for num in range(1, 21)]
print(numero)
'''one million
print numbers from one to one million'''
#million = [print(mil) for mil in range(1, 1000000)]
'''summing a million'''
million = [mil for mil in range(1, 1000000)]
print(sum(million))
'''odd numbers
print odd numbers between one and 20'''
odd = [od for od in range(1,20,2)]
print(odd)
'''threes
make a list of the multiples of 3 from 3 to 30'''
three = [thr for thr in range(3,30,3)]
print(three)
'''cubes
list of cubes from one to ten'''
cubes = [cube**3 for cube in range(1,11)]
print(cubes)
'''working with part of a list'''
print(cubes[:6])
print(cubes[3:5])
print(cubes[3:])
print(cubes[-3:])
'''Looping through a slice'''
for cube in cubes[:5]:
    print(cube)
'''copying a list'''
cubic = cubes[:]
print(cubic)
cubes.append(21**3)
cubic.append(22**3)
print(cubes,"\n",cubic)
'''slices exercises'''
print("These are the first three items in the list:")
print(cubes[:3])

print("Three items from the middle of the list are:")
print(cubes[3:6])

print("The last three items in the list:")
print(cubes[-3:])

print(foods)
'''my foods, your foods'''
friends_foods = foods[:]
friends_foods.append("kanyama")
foods.append("soya porridge")
print(foods)
print(friends_foods)
for food in foods:
    print(food)
print("The second foods")
for food in friends_foods:
    print(food)
'''Tuples'''
'''they are immutable'''
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
#print(dimensions[3])
tuple = (3, 4, 5, 6)
print(tuple)
'''printing individual items in a tuple through a loop'''
for tup in tuple:
    print(tup)
for dim in dimensions:
    print("{} is a part of dimension".format(dim))

print("This is the original dimension list:")
print(dimensions)

print("\n")
dimensions = (300, 500, 600, 80)
for dim in dimensions:
    print(dim)

'''five basic foods'''
basic_foods = ("ugali", "mboga", "eggs", "chapati", "beans")
for food in basic_foods:
    print(food)
#basic_foods[0] = "dengu" basic foods rejected because tuple is immutable
basic_foods = ("ugali", "mboga", "eggs", "dengu", "lentils")
print(basic_foods)
'''styling your code'''
'''they recommend PEP 8 to write your code
line length = should be less than 80 characters per line
BLANK LINES
Leave blank lines to group your codes
https://python.org/dev/peps/pep-0008/ for the PEP 8 guidelines'''
