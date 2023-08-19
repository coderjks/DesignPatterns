from random import randint


class Dice:

    def __init__(self, dice_count):
        self.dice_count = dice_count
        self._min = 1
        self._max = 6

    def roll(self):
        dice_used = 0
        dice_sum = 0

        while dice_used < self.dice_count:
            dice_sum += randint(self._min, self._max)
            dice_used += 1

        return dice_sum
