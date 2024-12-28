# Employee List
file_name = r'C:\Users\Bartek\Desktop\prg-basics\08-FileHandling\it_company.csv'

# Position
job_title = 'Software Engineer'

with open(file_name, 'r') as file:
    counter=1
    for line in file:
        if job_title in line:
            print(f"{counter}. {line.strip()}")
            counter+=1

