import json

product={}

product['name'] = input("Enter product name: ")
product['price'] = float(input("Enter product price: "))
paid_input = input("Has the product been paid for? (yes/no): ").strip().lower()

if paid_input=="y":
    product['paid']=True
elif paid_input=='n':
    product['paid']=False
else:
    print("Invalid input for 'paid' status. Assuming 'no'.")
    product['paid']=False


file_name = "product.json"

with open(file_name, 'w') as file:
    json.dump(product, file, indent=4)

print(f"Product data has been saved to {file_name}")
