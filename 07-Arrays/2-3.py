# Weekly expenses for different categories
# [Food, Transport, Utilities]
monthly_expenses = [
   [200, 50, 100],  # Week 1
   [180, 60, 110],  # Week 2
   [220, 55, 105],  # Week 3
   [210, 65, 95]    # Week 4
]

# Calculates expenses
# Use loop statements

total_food = 0
total_transport = 0
total_utilities = 0
weekly_totals = [0, 0, 0, 0]

for week in range(4):  #czemu in range(4) działa, a nie działa in monthly expenses?
    total_food+=monthly_expenses[week][0]
    total_transport+=monthly_expenses[week][1]
    total_utilities+=monthly_expenses[week][2]
    weekly_totals[week]= sum(monthly_expenses[week])

total_expenses = total_food+total_transport + total_utilities
# Print expenses
print('MONTHLY EXPENSES')
print('----------------')
print('Food:',total_food)
print('Transport:',total_transport)
print('Utilities:',total_utilities)
print('Week 1:',weekly_totals[0])
print('Week 2:',weekly_totals[1])
print('Week 3:',weekly_totals[2])
print('Week 4:',weekly_totals[3])
print('---------------')
print('TOTAL:', total_expenses)