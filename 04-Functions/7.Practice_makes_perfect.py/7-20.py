def f(number1,number2,number3):
    numbers=[number1,number2,number3]
    numbers.sort()
    return numbers[2] - numbers[0]

print(f(7,4,9))
print(f(2,12,8))