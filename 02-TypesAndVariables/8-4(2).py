# A program that prints your height both in cm and in feet and inches.

# Height in centimeters
cm = 170

# Conversion factors
cm_per_inch = 2.54  # 1 inch = 2.54 cm
cm_per_foot = 12  # 1foot = 30.48cm

# Convert cm to total inches
total_inches = cm // cm_per_inch  # Division without remainder to get total inches

# Calculate the number of feet (whole feet using division without remainder)
feet = total_inches // cm_per_foot  # Division without remainder

# Calculate the remaining inches (using remainder of division)
inches = total_inches % cm_per_foot  # Modulus (remainder of division)


# Output the result
print(f'I am {cm} cm tall, i.e. {int(feet)} feet and {inches:.0f} inches')
print(f'I am {cm} cm tall, i.e. {int(feet)} feet and {inches} inches')