import re  # module for regular expressions

# file name with shopping report
email_file = r"C:\Users\bkozi\Desktop\prg-basics\08-FileHandling\report.txt"

# read the content of email
with open(email_file, 'r', encoding='utf-8') as file:
    email = file.read()

# regular expression pattern for amounts (escaped dot)
pattern = r"€\d+"

# extract numbers from email
amounts = re.findall(pattern, email)

# Debugging: print extracted amounts
print("Extracted amounts:", amounts)

# calculate the total purchases
total = 0
for amount in amounts:
    total += float(amount[1:])  # convert string to float

# print result
print("Total:", total)
