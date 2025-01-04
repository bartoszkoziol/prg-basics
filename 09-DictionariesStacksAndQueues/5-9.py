import csv

# Krok 1: Wczytanie danych o prowincjach z pliku province.csv
province_dict = {}

with open(r'C:\Users\Bartek\Desktop\prg-basics\09-DictionariesStacksAndQueues\province.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        province_dict[row["Letter"]] = row["Name"]

# Krok 2: Inicjalizacja licznika pojazdów dla każdej prowincji
vehicle_count = {province: 0 for province in province_dict.values()}

# Krok 3: Wczytanie numerów rejestracyjnych pojazdów z pliku vehicle.txt i zliczanie pojazdów
with open(r'C:\Users\Bartek\Desktop\prg-basics\09-DictionariesStacksAndQueues\vehicle.txt', 'r', encoding='utf-8') as vehicle_file:
    for line in vehicle_file:
        vehicle_number = line.strip()  # Usunięcie zbędnych spacji lub znaków nowej linii
        first_letter = vehicle_number[0]  # Pierwsza litera numeru rejestracyjnego

        # Krok 4: Jeśli pierwsza litera odpowiada prowincji, zwiększ licznik
        if first_letter in province_dict:
            province = province_dict[first_letter]
            vehicle_count[province] += 1

# Krok 5: Wyświetlenie wyników
for province, count in vehicle_count.items():
    print(f"Pojazdy z {province}: {count}")
