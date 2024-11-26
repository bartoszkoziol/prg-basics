def print_unique_elements(array):
    unique_elements=[]
    for i in array:
        if array.count(i) == 1:
            unique_elements.append(i)
    
    print("Array: ", " ".join(map(str,array)))
    print("Unnique Array: ", " ".join(map(str, unique_elements)))

array = [2, 3, 2, 5, 8, 1, 9, 8]
print_unique_elements(array)