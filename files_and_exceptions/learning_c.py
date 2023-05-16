recap = 'learning_python.txt'
message = "Python"
with open(recap) as python_notes:
    for line in python_notes:
        if line == message:
            message.replace("Python", "C")
        print(line.rstrip())
    