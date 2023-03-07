first_name = "martin"
last_name = "luther"
full_name = "{} {}".format(first_name, last_name)

print(full_name)
print("Hello {}".format(full_name.title()))

message = "Hello {}".format(full_name.title())
print(message)

'''Adding white spaces with tabs and new lines'''
print("python")
print("\tpython")

print('Languages:\n\tpython\n\tC\n\tJavaScript')

'''Stripping white space'''

favourite_language = "python "
print(favourite_language)
print(favourite_language.rstrip())
favourite_language = "   python"
print(favourite_language)
print(favourite_language.lstrip())
print(favourite_language.strip())
