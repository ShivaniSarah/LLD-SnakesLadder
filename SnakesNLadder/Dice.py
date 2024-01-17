import random

class Dice:
    def __init__(self, dice_count):
        self.dice_count = dice_count
        self.min_value = 1
        self.max_value = 6

    def roll_dice(self):
        total_sum = 0
        dice_used = 0

        while dice_used < self.dice_count:
            total_sum += random.randint(self.min_value, self.max_value)
            dice_used += 1

        return total_sum

# # Example usage
# dice_instance = Dice(dice_count=2)
# result = dice_instance.roll_dice()
# print(f"Result of rolling the dice: {result}")
