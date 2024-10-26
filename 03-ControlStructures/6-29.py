N = int(input("Podaj liczbe N: "))

liczb_pierwszych = 0
liczba = 2

while liczb_pierwszych<N:
    jest_pierwsza=True  
    
    for i in range(2,liczba):
        if liczba % i ==0:
            jest_pierwsza=False
            break
    if jest_pierwsza:
        print(liczba, end=' ')
        liczb_pierwszych+=1
    liczba+=1