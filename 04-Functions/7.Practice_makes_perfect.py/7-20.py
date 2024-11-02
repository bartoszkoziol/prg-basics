def f(x,y,z):
    numbers = [x,y,z]
    numbers.sort()
    return numbers[2] - numbers[0]

print(f(7,4,9))
print(f(2,12,8))