def f(number):
    number = str(number)
    sum = 0
    t = [0] * 10
    for char in number:
        t[int(char)] += 1
    for i in range (10):
        if t[i] > 1:
            sum += t[i] * i
    return sum

#number = input('Enter number: ')
print(f(1027))