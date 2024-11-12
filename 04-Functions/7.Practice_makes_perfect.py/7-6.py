def f(binary_number):
    for char in binary_number:
        if char not in  ['0', '1']:
            return False
    return True

print(f("1100101"))      # Powinno zwrócić True
print(f("00000"))        # Powinno zwrócić True
print(f("123456"))       # Powinno zwrócić False
print(f("1a0b"))         # Powinno zwrócić False
print(f(""))             # Powinno zwrócić True, ponieważ pusty ciąg można traktować jako poprawny