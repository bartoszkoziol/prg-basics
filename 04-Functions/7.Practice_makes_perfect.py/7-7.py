def f(amount_to_pay):
    if amount_to_pay < 0:
       return "Kwota musi być większa lub równa zero."
    
    coins = [5,2,1]
    count = 0

    for coin in coins:
        while amount_to_pay >= coin:
            amount_to_pay-=coin
            count+=1
    return count

print(f(23))  # Powinno zwrócić 6
print(f(8))   # Powinno zwrócić 3
print(f(2))   # Powinno zwrócić 1
print(f(0))   # Powinno zwrócić 0