###
# Reads from file, line by line and prints numbered list of countries
#
with open("countries.txt") as file:
    counter = 1
    for line in file:
        print(f"{counter}. {line}", end="")
        counter+=1