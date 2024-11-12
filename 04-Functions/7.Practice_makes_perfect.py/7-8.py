def f(number,even):
    suma=0
    for char in str(number):
        digit=int(char)
        if (even and digit%2==0) or (not even and digit%2!=0):
            suma+=digit
    return suma
if __name__ == "__main__":
    print(f(3124, True))   # powinno zwrócić 6 (2 + 4)
    print(f(3124, False))  # powinno zwrócić 4 (3 + 1)
    print(f(20576, False)) # powinno zwrócić 12 (5 + 7)
    print(f(20576, True))  # powinno zwrócić 8 (2 + 0 + 6)
    print(f(13115, True))  # powinno zwrócić 0 (brak cyfr parzystych)