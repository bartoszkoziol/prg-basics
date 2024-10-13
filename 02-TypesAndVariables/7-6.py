#The speed of vehicles on a highway in Poland must be between 40 and 140 km/h. 
#Write a program that checks whether the vehicle speed entered from the keyboard is correct. 

velocity = float(input("Podaj predkosc samochodu(km/h): "))
velocity_ok = velocity >=40 and velocity <= 140
print(f"Podana predkosc samochodu jest dozwolona: {velocity_ok}")

