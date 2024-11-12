def f(palindrome):
    if palindrome == palindrome[::-1]:
        return True
    else:
        return False

print(f("radar")) #returns True
print(f("12-11-21")) #returns True
print(f("book")) #returns False)