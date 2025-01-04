from functools import reduce

numbers = [2,4,6,3,7,5]

valid_numbers = list(filter(lambda x: x%2==0, numbers))
print(valid_numbers)

sum_of_even_nums=reduce(lambda x,y: x+y, valid_numbers)
print(sum_of_even_nums)