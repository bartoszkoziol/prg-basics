def f(product_number):
    three_num_sum=0
    for digit in str(product_number)[:-1]:
        three_num_sum+=int(digit)
    return three_num_sum%7==int(product_number[3])
    
    

print(f("1082"))  # Expected: True
print(f("2035"))  # Expected: True
print(f("1114"))  # Expected: False
print(f("7071"))  # Expected: False