###
# Functions to read any data type from the keyboard
#
def input_string(message):
    user_input = input(message)
    return user_input

def input_integer(message):
    while True:
        try:
            user_input = int(input(message))
            return user_input
        except ValueError:  
            print("Nieprawidłowy wpis. Proszę wprowadzić poprawną liczbę całkowitą.")


def input_real(message):
    while True:
        try:
            real = float(input(message))
            return real
        except ValueError:
            print("Nieprawidłowy wpis. Proszę wprowadzić poprawną liczbę rzeczywistą.")


def input_boolean(message):
    while True:
        user_input = input(message)
        if user_input == 'y':
            return True
        elif user_input == 'n':
            return False
        else:
            print("ieprawidłowy wpis. Proszę wprowadzić 'y' (tak) lub 'n' (nie).")