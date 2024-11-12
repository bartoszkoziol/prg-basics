#Program tells if the name is a Polish female name

name = input("Enter your name: ")

if name.endswith('a'):
    print(f"{name} -- Polish female name")
else:
    print(f"{name} -- the name is not a Polish female name")