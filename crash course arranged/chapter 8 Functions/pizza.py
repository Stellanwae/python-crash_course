'''Passing an arbitrary number of arguments'''
def make_pizza(*toppings):
    print(toppings)
make_pizza("peperon", "onions", "soya")

'''any that starts with an * is an arbitrary argument
Passes this argument as a tuple'''


'''Mixing positional and arbitrary arguments'''
def make_pizza(size, *toppings):

    print("Making a {}-inch pizza with the following toppings:".format(size))
    for topping in toppings:
        print("- {}".format(topping))
    
make_pizza(16, "pepperoni")
make_pizza(12, "mushrroms", "green peppers", "extra cheese")