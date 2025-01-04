from queue import Queue

def kolejka_klientów():
    kolejka=Queue()
    ticker_num=1
    print("Wpisz `new' żeby dodać klienta, 'next' żeby obsluzc nastepnego badz 'exit'")
    while True:
        komenda=input("Podaj new/next/exit: ")
        if komenda=="new":
            kolejka.put(ticker_num)
            ticker_num+=1
        elif komenda=="next":
            if not kolejka.empty():
                nastepny=kolejka.get()
                print(f"Obsłuugujemy klienta {nastepny}")
            else:
                print("Nikogo w kolejce")
        elif komenda=="exit":
            break
        else:
            print("Zła komenda")

kolejka_klientów()