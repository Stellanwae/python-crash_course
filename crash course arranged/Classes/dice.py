from random import randint as rint
class Dice:
    def __init__(self, sides):
        self.sides = sides
    
    def roll_dice(self):
        roll = rint(1, self.sides)
        print(roll)

playing_dice = Dice(6)

playing_dice.roll_dice()
playing_dice.roll_dice()
playing_dice.roll_dice()
playing_dice.roll_dice()
playing_dice.roll_dice()
playing_dice.roll_dice()
playing_dice.roll_dice()
playing_dice.roll_dice()
playing_dice.roll_dice()
playing_dice.roll_dice()
playing_dice.roll_dice()

playing_dice2 = Dice(20)

playing_dice.roll_dice()
playing_dice.roll_dice()
playing_dice.roll_dice()
playing_dice.roll_dice()
playing_dice.roll_dice()
playing_dice.roll_dice()
playing_dice.roll_dice()
playing_dice.roll_dice()
playing_dice.roll_dice()
playing_dice.roll_dice()
playing_dice.roll_dice()

