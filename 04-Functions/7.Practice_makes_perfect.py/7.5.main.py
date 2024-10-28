from card_masker_module_7_5 import hide

def main():
    card_input = input("Podaj numer karty: ")

    result = hide(card_input)

    if result == "Nieprawidłowy numer karty. Numer musi mieć dokładnie 16 cyfr.":
        print(result)
    else:
        print(f"Zamaskowany numer karty: {result}") 
if __name__ == "__main__":
    main()  