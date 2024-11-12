from card_masker_module_7_5 import mask_credit_card

def main():
     # Pobranie numeru karty od użytkownika
    user_input = input("Podaj numer karty: ")

    masked_card = mask_credit_card(user_input)

    if masked_card == "Nieprawidłowy numer karty. Numer musi mieć dokładnie 16 cyfr.":
        print(masked_card)
    else:
        print(f"Zamaskowany numer karty: {masked_card}")

if __name__ == "__main__":
    main()  # Uruchamiamy program