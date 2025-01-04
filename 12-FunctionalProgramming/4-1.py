employees = ["SMITH Lucy","JONES Janet","LEE Jerry",
               "JACKSON Peter","JOHNSON Rick",
               "LEWIS Terry","CLARKE Robin"]

emp_J = list(filter(lambda x: x.split()[0].startswith("J"), employees))

print(emp_J)