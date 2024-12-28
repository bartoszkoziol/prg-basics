def compare(arr1,arr2):
    if len(arr1)!=len(arr2):
        return False
    for i in range(len(arr1)):
        if arr1[i]!=arr2[i]:
            return False
    return True

arrays = [
    (["water", "book", "sky"], ["water", "book", "sky"]),
    ([True, False], [True, False, True]),
    ([5, 3, 1], [5, 3, 1]),
    ([3, 2, 1], [3, 2])
]

for arr1,arr2 in arrays:
    print(f"Array1: {" ".join(map(str,arr1))}")
    print(f"Array2: {" ".join(map(str,arr2))}")

    if compare(arr1,arr2):
        print("Comparison: arrays are the same")
    else:
        print("Comparison: arrays are different")