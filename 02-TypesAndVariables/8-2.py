###
# Calculation of circle area and circumference 
#

# determine radius and PI values
r = float(input("Podaj promień okręgu: "))
pi_value = 3.14
# calculate area 
pole = pi_value*r**2
# calculate circumference 
obwod = 2*pi_value*r
# print results
print(f"The area is: {pole}")
print(f"The circumference is: {obwod}")