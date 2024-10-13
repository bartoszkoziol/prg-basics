###
# A program that enables a user to challenge a computer.
# The computer throws dice. Then, the user then tries to guess
# the number from dice by entering a number from 1 to 6
# from the keyboard. If the user has guessed the number
# from the dice, the computer displays True. Otherwise,
# the computer displays False.
#
import random

# COMPUTER TURN
computer = random.randint(1,6)
print(computer)  #potem do usuniecia
# YOUR TURN
user_number = int(input("Try to guess which number i rolled (1-6): "))

#if user_number == computer:
    #print('You won')
#else:
    #print('You lost')
user_number_correct = user_number == computer
print(f"You guessed my number: {user_number_correct}")


