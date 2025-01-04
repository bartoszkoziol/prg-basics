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

try:
    with open(file_name, 'r') as file:
        existing_procucts=json.load(file)
        if not isinstance(existing_procucts, list):
            existing_procucts=[]
except FileNotFoundError:
    existing_procucts=[]

existing_procucts.append(product)

with open(file_name, 'w') as file:
    json.dump(existing_procucts, file, indent=4)

print(f"Product data has been saved to {file_name}")
