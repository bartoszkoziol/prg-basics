import re 

names=["Fin Bindeballe", 
       "Geir Anders Berge",
       "Shoil",
       "Ron Cambrige"
]

regex = r"^\w+ \w+$"

for name in names:
    result = re.search(regex, name)
    if result:
        print(name)