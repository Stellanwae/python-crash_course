def print_models(unprinted_designs, completed_models=[]):
    while unprinted_designs:
        complete = unprinted_designs.pop()
        completed_models.append(complete)
        print('Printing model: {}'.format(complete))

def show_completed_models(completed_models):
    print('The following models have been printed:')
    for model in completed_models:
        print(model)
