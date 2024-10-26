dec_number = int(input("Podaj liczbe w systemie dziesietnym: "))

bin_digits = []

while dec_number >0:
    remainder = dec_number%2
    bin_digits.insert(0, str(remainder))
    dec_number = dec_number//2

bin_number=''.join(bin_digits)
print(f" Liczba {dec_number} w systemie binarnym to {bin_number}")