def f(n):
    if n == 0:
        return 0
    if n == 1:
        print('*', end='')
    else: 
        print('*/', end='')
        f(n-1) 

n = int(input('Enter number: '))
f(n)