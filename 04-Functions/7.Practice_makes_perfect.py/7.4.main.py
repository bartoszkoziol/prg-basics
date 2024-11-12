from num_in_range_module7_4 import is_in_range

def main():
    number = int(input("Podaj liczbę: "))

    x,y = 2,15

    #if number is_in_range(x,y):                                    ### tutaj bez number  
        #print("Podana liczba należy do przedziału <2,15>")         ### w argumentach powinno być(number,x,y) a przed tym is_in_range
    #elif number not is_in_range(x,y):                              ### wtedy aktywuje się funkcja
        #print("Liczba nie należy do przedziału <2,15>")
    #else:
        #return "Podaj właściwą liczbę"

###tu jest poprawnie:
    if is_in_range(number,x,y):
        print("Podana liczba należy do przedziału <2,15>")
    else:
        print("Liczba nie należy do przedziału <2,15>")
        
if __name__ == "__main__":
    main()