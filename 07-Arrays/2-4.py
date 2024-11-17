# Weekly meal plan data (Breakfast, Lunch, Dinner)
weekly_meal_plan = [
    ["Oatmeal", "Grilled Chicken Salad", "Spaghetti"],  # Monday
    ["Pancakes", "Turkey Sandwich", "Grilled Salmon"],  # Tuesday
    ["Eggs", "Chicken Caesar Salad", "Pizza"],  # Wednesday
    ["Smoothie", "Veggie Wrap", "Stir-fried Beef"],  # Thursday
    ["Bagel", "BLT Sandwich", "Salmon Fillet"],  # Friday
    ["Cereal", "Fish Tacos", "Steak"],  # Saturday
    ["Toast", "Grilled Cheese", "Pasta"]  # Sunday
]

# List of days of the week
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# Print the weekly meal plan
print("WEEKLY MEAL PLAN")
print("(Breakfast, Lunch, Dinner)")
print("==========================")

# Iterate through each day and corresponding meals
for day in range(7): #lub in range(len(weekly_meal_plan))
      print(f"{days_of_week[day]}: {", ".join(weekly_meal_plan[day])}")
     
