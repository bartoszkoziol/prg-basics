def f(dice):
    if not dice:  # Sprawdzenie, czy ciąg wejściowy jest pusty
        return None  # lub można zwrócić 0 albo zgłosić wyjątek w zależności od wymagań

    max_count = 1  # Aby śledzić maksymalną liczbę wystąpień kolejnych cyfr
    current_count = 1  # Aby zliczać aktualną cyfrę
    current_digit = dice[0]  # Rozpocznij od pierwszej cyfry
    max_digit = current_digit  # Aby śledzić cyfrę z maksymalną liczbą wystąpień

    for i in range(1, len(dice)):
        if dice[i] == current_digit:
            current_count += 1  # Zwiększ licznik, jeśli ta sama cyfra została znaleziona
        else:
            # Zaktualizuj max_count i max_digit, jeśli current_count jest większe
            if current_count > max_count:
                max_count = current_count
                max_digit = current_digit
            # Zresetuj dla nowej cyfry
            current_digit = dice[i]
            current_count = 1

    # Ostateczna kontrola, aby zaktualizować max_count i max_digit dla ostatniej sekwencji
    if current_count > max_count:
        max_digit = current_digit

    return int(max_digit)  # Zwróć cyfrę, która ma maksymalną liczbę wystąpień

# Przykład użycia:
print(f("5233165554211"))  # Wynik: 5
print(f("2133"))           # Wynik: 3