###
# Program for testing built-in functions
#
max_number = max(7,5,6,3,8,2)
print('Max number of 7,5,6,3,8,2 is', max_number)

min_number = min(4,7,2,3,9,8)
print('Min number of 4,7,2,3,9,8 is', min_number)

str_length = len("computer science")
print('The number of characters in "computer science" is', str_length)

letter = input("Enter a letter: ")
print(f"You entered the letter: {letter}")

number_str="20303"
number=int(number_str)
print(number)

decimal_num = int(input("Enter decimal number: "))
binary_num=bin(decimal_num)
print(binary_num)

decimal_num2=int(input("Enter decimal number: "))
hex_num=hex(decimal_num2)
print(hex_num)

sign=(input("Enter your sign: "))
unicode_code=ord(sign)
print(f"Kod Unicode dla znaku '{sign}': {unicode_code}")

value=-17
abs_value=abs(value)
print(abs_value)

