def f(name):
    acronym=""
    for word in name.split():
        first_letter=word[0]
        acronym+=first_letter
        #lub acronym+=word[0]
    return acronym
    
print(f("Internet of Things"))
print(f("For Your Information"))