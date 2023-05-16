try:
    print('Give me two numbers to divide')
    num1 = int(input())
    num2 = int(input())
    division = num1 / num2
    print(division)
except ValueError:
    print('Please write a number')
