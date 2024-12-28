###
# Reads from file, line by line and prints numbered list of countries
#
with open('countries.txt', 'r') as file:
    for line in file:
        print(line, end="")