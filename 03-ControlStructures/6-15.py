code=input("Enter EAN-13 article number: ")


if len(code)==13 and code.isdigit():
    print("The code is valid")
    if code[:3]=="590":
        print("This is polish product")
else:
    print("The code is invalid")
