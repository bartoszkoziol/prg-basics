def f(n):
    if n==1:
        return 0
    elif n==2 or n==3:
        return 1
    else: 
        return f(n-1) + f(n-2)
    

print(f(5)) #returns 3
print(f(9)) #returns 21

#0 1 1 2 3 5 8 13 21