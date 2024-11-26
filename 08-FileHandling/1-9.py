###
# Prints employees employed in a specified position.
#

# Employee List
file_name = 'it_company.csv1'

# Position
job_title = 'Software Engineer'

counter = 1
with open("it_company.csv", 'r') as file:
   
   for line in file:
    if job_title in line:
        print(f"{counter}. {line}", end="")
        counter+=1