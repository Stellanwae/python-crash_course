def get_formatted_name(first_name, last_name):
 """Return a full name, neatly formatted."""
 full_name = f"{first_name} {last_name}"
 return full_name.title()

while True:
 print('\Please enter your name:')
 print('You are free to type q to quit')
 f_name = input('First_name: ')
 if f_name == 'q':
  break
 l_name = input('Last name: ')
 if l_name == 'q':
  break
 formated_name = get_formatted_name(f_name, l_name)
 print('Hello {}'.format(formated_name))