def bubblesort(array):
    n = len(array)
    # Wykonujemy n-1 przejść przez tablicę
    for i in range(n):
        for j in range(0, n-i-1):
            # Jeśli element jest większy od następnego, zamieniamy je miejscami
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

# Przykłady użycia funkcji
array1 = [64, 34, 25, 12, 22, 11, 90]
array2 = [5, 3, 8, 2, 7, 1]
array3 = [45, 78, 12, 56, 23, 89, 90]

# Sortowanie tablic
sorted_array1 = bubblesort(array1)
sorted_array2 = bubblesort(array2)
sorted_array3 = bubblesort(array3)

# Wyświetlanie wyników
print("Posortowana array1:", sorted_array1)
print("Posortowana array2:", sorted_array2)
print("Posortowana array3:", sorted_array3)
