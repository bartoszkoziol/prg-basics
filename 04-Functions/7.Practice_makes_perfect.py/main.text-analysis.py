from text_analysis import count_letter

def main():
    # Tekst do analizy
    text = "You never get a second chance to make a first impression"

    # Litera do zliczenia
    letter = 'e'

    # Wywołanie funkcji i uzyskanie liczby wystąpień litery
    count = count_letter(text,letter)

    # Wyświetlenie wyniku
    print(f"Liczba wystąpień litery {letter}: {count}")

if __name__ == "__main__":
    main()