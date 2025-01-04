names = [("Smith","Lucy"),("Jones","Janet"),("Lee","Jerry"),
   ("Jackson","Peter"),("Johnson","Rick"),
   ("Lewis","Terry"),("Clarke","Robin")]

#result = list(map(lambda surname, name:surname.upper()+","+name, names ))
result = list(map(lambda name: name[0].upper()+", "+name[1], names))
for x in result:
    print(x)