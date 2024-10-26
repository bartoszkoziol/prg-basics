# Ustawiamy liczby w przedziale od 1 do 49
liczba = 1

for kolumna in range(7):
    for wiersz in range(7):
        print(kolumna+wiersz*7+1, end=' ')
    print()
  