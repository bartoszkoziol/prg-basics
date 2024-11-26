import csv
with open(r'C:\Users\bkozi\Desktop\prg-basics\08-FileHandling\it_company.csv', 'r') as file:
    content = csv.DictReader(file)

    print('GRAPHIC DESIGNERS')
    print("=================")

    for row in content:
        if row['Job Title'] == "Graphic Designer":
            print(f"{row["First Name"]} {row["Last Name"]}, {row["Email"]}")