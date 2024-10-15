# Program, który wyświetla Twoją wysokość zarówno w cm, jak i w stopach oraz calach.

cm = 170  # Twoja wysokość w centymetrach

# Obliczanie stóp i cali
stopy = cm // 30.48  # Całkowite stopy
pozostałe_cm = cm % 30.48  # Pozostałe centymetry po całkowitych stopach
cale = pozostałe_cm / 2.54  # Konwersja pozostałych centymetrów na cale

# Wyświetlanie wyników
print(f'Mam {cm} cm wzrostu, co odpowiada {stopy} stopom i {cale:.2f} calom')