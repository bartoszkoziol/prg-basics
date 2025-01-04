import matplotlib.pyplot as plt

# Dane temperatur w miastach
measurements = {"Krakow": 7, "Warszawa": -2, "Sopot": 4, "Koszalin": -1, "Opole": 3}

# Użycie map() do stworzenia dwóch list: miast i temperatur
cities = list(map(lambda x: x[0], measurements.items()))  # nazwy miast
temperatures = list(map(lambda x: x[1], measurements.items()))  # temperatury

# Tworzenie wykresu słupkowego
plt.bar(cities, temperatures)

# Dodanie tytułu oraz etykiet osi
plt.title("Temperatures Recorded in Cities")
plt.xlabel("Cities")
plt.ylabel("Temperature (°C)")

# Wyświetlenie wykresu
plt.show()