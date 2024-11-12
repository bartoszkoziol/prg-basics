def f(number):
    number=str(number)
    suma_powtaralnych=0
    for i in number:
        ile_razy=number.count(i)
        if ile_razy>1:
            suma_powtaralnych+=int(i)
    return suma_powtaralnych
print(f(1027))       # Wynik: 0 (brak powtarzających się cyfr)
print(f(230335))     # Wynik: 8 (tylko 3 i 5 powtarzają się)
print(f(513553007))  # Wynik: 5 (tylko 5 powtarza się)