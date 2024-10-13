#Dice rolled: 4
#Special number (1 or 6): False
import random

dice_roll_1 = random.randint(1,6)
special_number = dice_roll_1 == 1 or dice_roll_1 == 6
print(f"Dice rolled number: {dice_roll_1}")
print(f"Special number: {special_number}")