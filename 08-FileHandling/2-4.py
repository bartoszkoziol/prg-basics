###
# Saves to a file a list of employees working at a specified position.
#

# file names
employees_file = r"C:\Users\bkozi\Desktop\prg-basics\08-FileHandling\it_company.csv"
position_file = 'software_engineer.txt'

# Position
job_title = 'Software Engineer'

# write selected employees to a file
with open(employees_file, 'r') as employees:
   with open(position_file, 'w') as output_file:
      for line in employees:
         if job_title in line:
            output_file.write(line)

