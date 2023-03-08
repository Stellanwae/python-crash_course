active_poll = True
dream_vacation = {}
while active_poll:
    name = input('what is your name? ')
    prompt = input('If you could visit a place, where would you go? ')
    repeat = input('would you like to repeat the poll? ')
    dream_vacation[name] = prompt
    if repeat == 'no':
        active_poll = False

for k, v in dream_vacation.items():
    print('{} would love to go to {}'.format(k, v))
