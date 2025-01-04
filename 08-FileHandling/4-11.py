with open('powers.txt', 'w') as file:
    for i in range(1,101):
        second_power=i**2
        third_power=i**3

        file.write(f"{i}, {second_power}, {third_power}\n")