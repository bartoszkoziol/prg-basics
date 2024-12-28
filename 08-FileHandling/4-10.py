import csv

file_path = r"C:\Users\bkozi\Desktop\prg-basics\08-FileHandling\clothing.csv"

with open(file_path, 'r') as file:
    content = csv.DictReader(file)

    print("Products with Price < 60 and Stock < 40")
    print("=======================================")

    for row in content:
        price = float(row["Price"])
        stock = int(row["Stock_Quantity"])

        if price<60 and stock<40:
            print(f"{row["Product_ID"]}: Price: {price}, Stock: {stock}")
