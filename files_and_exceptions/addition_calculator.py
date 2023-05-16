try:
    while True:
        print('Give me two numbers so that I divide for you')
        num1 = int(input())
        num2 = int(input())
        div = num1 / num2
    
except ValueError:
    print('Please retype a number')

else:
    print(div)