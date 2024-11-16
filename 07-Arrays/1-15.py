car_fuel_consumption = [7.2, 6.8, 7.5, 7.0, 7.1, 6.9, 7.3]
bank_transactions = [-150, -20, 300, -45, -60, 500, -120]
###
# Bubble sort
#
def bubble_sort(arr):
   n = len(arr)
   for i in range(n):  # Iteracja przez elementy listy
      for j in range(0, n - i - 1):  # Iteracja przez nieposortowaną część listy
         if arr[j] > arr[j + 1]:  # Jeśli elementy są w złej kolejności
            arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Zamiana miejscami
   return arr

car_fuel_consumption = car_fuel_consumption  # Oryginalna lista
print(car_fuel_consumption)  # Wyświetlenie oryginalnej listy
sorted_car_fuel_consumption = bubble_sort(car_fuel_consumption) 
print(sorted_car_fuel_consumption)  # Wyświetlenie posortowanej listy

bank_transactions = bank_transactions  # Oryginalna lista
print(bank_transactions)  # Wyświetlenie oryginalnej listy
sorted_bank_transactions = bubble_sort(bank_transactions)
print(sorted_bank_transactions)  # Wyświetlenie posortowanej listy