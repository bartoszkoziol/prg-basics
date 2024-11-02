def f(password):
    if len(password) < 6:
        return False
    
    if len(set(password)) != len(password): # len 
        return False
    
    return True

print(f("abcdef"))  # Returns True (valid password)
print(f("abcde"))   # Returns False (too short)
print(f("abcdeff")) # Returns False (duplicate characters)
print(f("123456"))  # Returns True (valid password)
print(f("12345a"))  # Returns False (too short)
print(f("aabbcc"))  # Returns False (duplicate characters)