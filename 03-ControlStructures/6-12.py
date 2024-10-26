#A program that calculates the amount to be paid in the shop 

product_num = int(input("Podaj liczbe zakupionych produktow: "))
product_price = float(input("Podaj cene produktu: "))

if product_num>2:
    total_cost=product_price*2
    total_cost+=(product_num-2)*product_price*0.75
else:
    total_cost=product_num*product_price

print(f"Amount to pay is {total_cost}")