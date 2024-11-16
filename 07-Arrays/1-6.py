###
# Returns the name of the day of the week for a given day number (1-Monday ... 7-Sunday)
#
def weekday(n):
      weekdays = ["Monday", "Tuesday", "Wednesday",
         "Thursday", "Friday", "Saturday", "Sunday"]
      return weekdays[n-1]

print("Day 1: ", weekday(1))
print("Day 4: ", weekday(4))
print("Day 7: ", weekday(7))