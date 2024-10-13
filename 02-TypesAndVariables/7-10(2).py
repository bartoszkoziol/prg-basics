import random

computer = random.randint(1,6)
print(computer)

user_number = int(input("Sprobuj zgadnac moj numer: "))
is_correct = user_number == computer
print(f"Zgadles moj numer: {is_correct}")