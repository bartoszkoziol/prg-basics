speeds=[48,47,54,50,42,68,39,46]

# def is_correct_speed(speed):
#     return speed>50

higher_speeds = list(filter(lambda speed:speed>50, speeds))
print(higher_speeds)