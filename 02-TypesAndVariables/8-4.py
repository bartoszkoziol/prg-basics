###
# A program that prints your height both in cm and in feet and inches.
#
cm = 170
#dzielenie z resztą
feet = cm/30.48
inches = cm/2.54

#dzielenie bez reszty
feet_2 = round(cm//30.48)
inches_2 = round(cm / 2.54)

print(f'I am {cm}cm tall, i.e. {feet} feet and {inches} inches')
print(f'I am {cm}cm tall, i.e. {feet_2:.0f} feet and {inches_2:.0f} inches')