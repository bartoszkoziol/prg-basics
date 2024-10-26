#The parking meter calculator
hours = int(input("Tell me how many hours u were on the parking: "))

if hours in range(1,3):
    print("Gimme 5 PLN")
elif hours in range(3,7):
    print("Gimme 15 PLN")
elif hours>6:
    print("Gimme 20 PLN")
else:
    print("You're free to go")