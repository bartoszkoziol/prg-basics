###
# Prints some array elements
#
arr = [2, 3, 7, 5, 4]

print(arr)
print('Number of elements', len(arr))
print('First value', arr[0])
print('Second value', arr[1])
print('Last value', arr[-1])
print('Last but one value', len(arr)-1)
print("sum of the first and second", arr[0]+arr[-1])
print("Middle value", arr[len(arr)//2] )
for char in range(len(arr)): #?
    print(str(char) + " ",end=" ")