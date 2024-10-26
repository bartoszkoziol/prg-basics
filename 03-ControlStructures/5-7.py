import time

seconds=int(input("Podaj liczbę sekund do odliczenia: "))

number_to_words = {
    5: "pięć",
    4: "cztery",
    3: "trzy",
    2: "dwa",
    1: "jeden"
}

while seconds>0:
    if seconds in number_to_words:
        print(number_to_words[seconds])
    else:
        print(seconds)
    time.sleep(1)
    seconds-=1
print("Czas uplynal!")