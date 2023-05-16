from random import choice
lottery = ["one", "two", "three", "four", "five", 3, 4, 56, 67, 76, 34, 78, 90, 23, 32]

win = choice(lottery)
win1 = choice(lottery)
win2 = choice(lottery)
win3 = choice(lottery)

print(f"{win} {win1} {win2} {win3}")

