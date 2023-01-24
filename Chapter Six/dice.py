from random import randint


class Die:
    """An attempt to create a dice"""

    def __init__(self, sides=6):
        """Initialize the default attributes"""
        self.sides = sides
        self.roll = 0

    def roll_dice(self):
        self.roll = randint(1, self.sides)
        print('The dice stopped at: ' + str(self.roll))


my_dice = Die()
my_dice.roll_dice()
