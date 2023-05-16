recap = "learning_python.txt"
'''Printing file contents by reading through the entire file'''
with open(recap) as file_content:
    read_recap = file_content.read()
print(read_recap)

'''Printing an entire file using a loop'''
with open(recap) as my_file:
    for line in my_file:
        print(line.rstrip())

'''Looping the entire file and working with them
outside the block'''
my_string = ""
with open(recap) as python_notes:
    read_python_notes = python_notes.readlines()

for note in read_python_notes:
    my_string =+ note

print(my_string)