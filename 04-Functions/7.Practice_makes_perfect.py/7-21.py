def f(name):
    acronym=""
    for word in name.split():
        acronym+=word[0]
    return acronym


print(f("Internet of Things"))
print(f("For Your Information"))