###
# Checks whether at least one number entered
# from the keyboard is not negative
# 
x = int(input('Enter first number: '))
y = int(input("Enter second number: "))

if not x < 0 or not y < 0 : #ważne aby tutaj dodać nawias, bo inaczej kod nie działa prawidłowo
    #if not (x < 0 and y < 0) to jest to samo co if not x < 0 or not y < 0
    print(f'At least one of the numbers {x} and {y} is not negative')
else: 
    print("Both nubmers are negative")