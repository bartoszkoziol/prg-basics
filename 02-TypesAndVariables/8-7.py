#decimal to binar and hexadecimal converter

input_number = int(input("Enter your number: "))

bin_number = bin(input_number)[2:]
hex_number = hex(input_number)[2:].upper()

print(f"{input_number} is equal to {bin_number} in binary system")
print(f"{input_number} is equal to {hex_number} in hex system")