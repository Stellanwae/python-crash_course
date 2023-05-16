file_name = "pi_digits.txt"

with open(file_name) as file_content:
    lines = file_content.readlines()

pi_string = ""
for line in lines:
    pi_string =+ line.rstrip()

print(pi_string)