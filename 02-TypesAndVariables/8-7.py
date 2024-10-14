#decimal to binar and hexadecimal converter

number = int(input("Podaj liczbę, którą chcesz przekonwertować: "))

binar = bin(number)[2:]  #[2:] pobieramy wycinek zaczynajac od 2 miejsca hello = llo
hex = hex(number)[2:].upper()


print(f"Liczba {number} w systemie binarnym to {binar}")
print(f"Liczba {number} w systemie szesnastkowym to {hex}")