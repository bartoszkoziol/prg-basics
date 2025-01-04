last_bottles = [508,500,512,499,492,511,503,476,501,509]

tolerance=0.02
lower_limit=500*0.98
upper_limit=500*1.02

incorrect_bottles=[bottle for bottle in last_bottles if bottle<lower_limit or bottle>upper_limit]

percentage_incorrect=(len(incorrect_bottles)/len(last_bottles))*100

print(f"Bottle capacity:      500ml")
print(f"Filling tolerance:    2%")
print(f"Filled bottles:       {', '.join(map(str,last_bottles))}")
print(f"Incorrectly filled:   {percentage_incorrect:.0f}%")