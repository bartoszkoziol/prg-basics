results=[37,51,44,23,78,92,39,84,83,51]

def min_pts(limit):
   return lambda pts: pts>=limit

print("Min 70 pts: ", list(filter(min_pts(70), results)))
print("Min 40 pts: ", list(filter(min_pts(40), results)))
print("Min 30 pts: ", list(filter(min_pts(30), results)))

