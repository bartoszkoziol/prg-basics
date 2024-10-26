#Program that calculates dog age into human age

human_years=float(input("Enter your dog age in human years: "))

if human_years<=2:
    dog_years = human_years * 10.5
else:
    dog_years=10.5*2+(human_years-2)*4

print(f"Your dog is {dog_years} years old")    