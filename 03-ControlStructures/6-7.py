#Age and group you belong to checker
age = int(input("Enter your age: "))

if age < 13:
    print("You are a child")
elif age in range(13,20):
    print("You are a teen") 
elif age in range(20,65):
    print("You are an adult")
elif age >=65:
    print("You are a senior")