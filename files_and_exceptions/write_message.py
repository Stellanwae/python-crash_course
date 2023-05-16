file = "programming.txt"
with open(file, "w") as file_object:
    file_object.write("I love programming")
    file_object.write("You should try programming")

'''appeninding to a file'''
with open(file, 'a') as file_object:
    file_object.write("I love programming")
