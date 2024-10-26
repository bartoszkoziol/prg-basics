###
# Calculates the sum of the digits in a number
#
def sum_digits(number):
    number=abs(number)
    number_str=str(number)

    total_sum=0

    for digit in number_str:
        total_sum+=int(digit)

    return total_sum
    
any_number = int(input('Enter integer number: '))
result = sum_digits(any_number)
print(f'The sum of the digits in the number {any_number} is {result}')