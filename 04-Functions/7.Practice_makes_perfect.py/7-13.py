def f(number1,number2,operator):
    if operator == "+":
        return number1 + number2
    elif operator == "-":
        return number1 - number2
    elif operator == "*":
        return number1*number2
    elif operator == "%":
        return number1%number2
    elif operator == "**":
        return number1**number2
    else:
        return "Enter valid operator"

print(f(2,3, "+")) #returns 5
print(f(2,3, "%")) #returns 2
f(2,3, "**") #returns 8
f(2,3, "*") #returns 6
f(2,3, "-") #returns -1