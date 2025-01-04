grades = [3.0,5.0,2.0,3.5,4.0,4.0,3.5,2.0,4.0,2,0]

correct_grades = list(filter(lambda grade: grade>2, grades))
arithmeic_mean = sum(correct_grades)/len(correct_grades)
print(f"Arithmetic mean for grades greater than 2.0 is: {arithmeic_mean:.2f}")


