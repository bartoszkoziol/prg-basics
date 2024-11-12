###
# A program that reads a SWIFT code from the keyboard
# and prints the bank code and country code.
#
swift = input("Enter your SWIFT code: ")

bank_code = swift[:4]
country_code = swift[4:6]
print(f'Bank Code: {bank_code}')
print(f'Country Code: {country_code}')

###lub można też tak krócej

#swift = input('Enter SWIFT code: ')
#print(f'Bank Code: {swift[:4]}')
#print(f'Country Code: {swift[4:6]}')