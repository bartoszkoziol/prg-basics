###
# Calculates the area of a triangle based on the lengths
# of the triangle's sides
#
import math

def triangle_area(a,b,c):
    p=0.5*(a+b+c)
    triangle_area=math.sqrt(p*(p-a)*(p-b)*(p-c))
    return triangle_area



print(f'The area of ​​a triangle with sides 3,4,5 is {triangle_area(3,4,5)}')
print(f'The area of ​​a triangle with sides 5,12,13 is {triangle_area(5,12,13)}')
print(f'The area of ​​a triangle with sides 7,24,25 is {triangle_area(7,24,25)}')