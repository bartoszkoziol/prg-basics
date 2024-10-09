###
# A program that calculates the volume
# and surface area of ​​a cuboid with sides a, b, and c.
# Read the dimensions of the cuboid from the keyboard.
#
a = input('a=')
b= input("b=")
c=input("c=")
a=int(a)
b=int(b)
c=int(c)

volume = a*b*c
cub_surface = 2*a*b+2*b*c+2*a*c
print(f"The volume of a cuboid with sides a={a}, b={b}, c={c} is {volume} ")
print(f"The surface area of the cuboid with sides a={a}, b={b}, c={c} is {cub_surface}")
