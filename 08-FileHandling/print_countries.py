###
# Reads from file, line by line
#
with open(r'C:\Users\Bartek\Desktop\prg-basics\08-FileHandling\countries.txt', 'r') as file:
    counter=1
    for line in file:
        # print(line, end="")
        print(f"{counter}. {line}",end="")
        counter+=1