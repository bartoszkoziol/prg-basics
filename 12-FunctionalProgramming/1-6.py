avg_speed=lambda distance,hours, minutes: distance/(hours+(minutes/60))

distance=float(input("Enter distance: "))
hours=int(input("Enter hours: "))
minutes=int(input("Enter minutes: "))

average_speed=avg_speed(distance,hours, minutes)
print(f" Average speed: {average_speed:.1f} km/h")

