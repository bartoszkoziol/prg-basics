def is_prime(number):
    if number<2:
        return False
    for i in range(2,number):
        if number%i==0:
            return False
    return True

def f(n):
    count=0
    number=1
    nth_prime=0

    while count<n:
        number+=1
        if is_prime(number): #Każdorazowo, gdy funkcja is_prime(number) zwróci True, co oznacza, że number jest liczbą pierwszą, wykonują się następujące kroki:
            count+=1 #count zwiększa się o 1
            nth_prime=number #nth_prime jest aktualizowane na wartość number
    return nth_prime

print(f(1)) #returns 2
print(f(3)) #returns 5
print(f(5)) # returns 11