squares =[]

for value in range(1, 11):
    square = value ** 2
    squares.append(square)
print(squares)

'''simple statistics with a range of numbers'''
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
'''minimum digits'''
print(min(digits))
'''maximum digits'''
print(max(digits))
'''sum of digits
'''
print(sum(digits))

'''List comprehensions
writing codes in the shortest way possible'''
squares = [value ** 2 for value in range(1, 11)]
print('This is from list comprehension')
print(squares)