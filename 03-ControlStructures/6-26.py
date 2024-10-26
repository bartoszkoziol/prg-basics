correct_pin = "0805"
attempts = 3

for attempt in range(attempts):
    pin = input("Enter your PIN: ")
    if pin == correct_pin:
     print("Access granted")
     break
    else:
        print("Incorrect PIN")
        if attempt == attempts - 1:
            print("Sorry, your payment card has been blocked.")
