###
# A program that calculates
# how many letters are between two given letters
#
first = input('Enter first letter: ')
last = input('Enter last letter: ')
first_letter_code = ord(first)
last_letter_code = ord(last)
## Obliczenie liczby liter między dwoma podanymi literami
number_of_letters = last_letter_code - first_letter_code - 1
print(f'Between {first} and {last} is {number_of_letters} letters')