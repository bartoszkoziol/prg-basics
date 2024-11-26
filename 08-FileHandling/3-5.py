###
# Checks the correctness of username and password
#
import re

# read username and password from keyboard
username = input("Enter username: ")
password = input("Enter password: ")

# pattern (criteria) for username and password
username_pattern = r"^[a-z]{6,}"
password_pattern = r"[A-za-z0-9_]{8,}"

# check if username and password are ok
username_match = re.match(username_pattern,username)
password_match = re.match(password_pattern, password)

# print results
if username_match and password_match:
   print("Username and password meet the requirements")
else:
   if not username_match:
       print("Invalid username: Must be at least 6 characters long and contain only lowercase letters.")
   if not password_match:
        print("Invalid password: Must be at least 8 characters long and contain only letters, numbers, or underscores.")