def suma(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    return n+suma(n-1)

print(suma(10))
