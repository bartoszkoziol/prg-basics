def f(password):
    if len(password) < 6:
        return False
    return len(set(password))==len(password)

print(f("ax15")) #returns False
print(f("book123")) #returns False
print(f("A2water3")) #returns True
print(f("qwerty")) #returns True
print(f("")) #returns False