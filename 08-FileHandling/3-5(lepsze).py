import re


username_pattern = r"^[a-z]{6,}"
password_pattern = r"[A-za-z0-9_]{8,}"

while True: 
    username = input("Enter username: ")
    password = input("Enter password: ")

    username_match = re.match(username_pattern,username)
    password_match = re.match(password_pattern, password)

    if username_match and password_match:
        print("Username and password meet the requirements")
        break
    else:
        if not username_match:
            print("Invalid username: Must be at least 6 characters long and contain only lowercase letters.")
        if not password_match:
            print("Invalid password: Must be at least 8 characters long and contain only letters, numbers, or underscores.")