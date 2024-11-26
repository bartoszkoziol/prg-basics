products = {
'Laptop': 15,
'Desktop PC': 10,
'Monitor': 25,
'Keyboard': 50,
'Mouse': 60,
'External Hard Drive': 30,
'Printer': 12,
'Router': 20,
'USB Flash Drive': 100,
'Graphics Card': 8
}

for name, quantity in products.items():
    print(f"{name}: {quantity}")

total_sum=0
for name, quantity in products.items():
    total_sum+=quantity
print(total_sum)