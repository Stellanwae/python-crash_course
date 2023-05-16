'''
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
print(contents)
'''

'''file paths
file_path = "/home/ehmathhes/other_files/text_files/file_name.txt
with open(file_path) as file_object:
    content = read(file_object)
print(contents.rstrip())
file paths
with open('text_file/filename.txt')'''

'''
Printing each member of the file in a loop

with open('file.txt') as line:
    for lin in line:
        print(lin.rstrip())

'''
with open('pi_digits.py') as file_content:
    lines = file_content.readlines()
for line in lines:
    print(line.rstrip())

