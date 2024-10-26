q1=input(" Are you interested in computer science? (y/n):").lower()=='y'
q2=input("Do you like playing computer games? (y/n):").lower()=='y'
q3=input("Do you have an Instagram account? (y/n):").lower()=='y'

print("SURVEY RESULTS: ")
print(f"Interested in computer science: {"Yes" if q1 else 'No'}")
print(f"Interested in playing computer games: {"Yes" if q2 else 'No'}")
print(f"Have and instagram account: {"Yes" if q3 else 'No'}")
