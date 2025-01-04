file_name = r'C:\Users\Bartek\Desktop\prg-basics\08-FileHandling\it_company.csv'
 

with open(file_name, 'r', encoding="utf-8") as file:
    lines=file.readlines()

    index=0
    while index<len(lines):
        for line in lines[index: index+5]:
            print(line.strip())
        index+=5


        if index<len(lines):
            input("Press Enter key...")

