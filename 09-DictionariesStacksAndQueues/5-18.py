# import json 

# with open(r'C:\Users\Bartek\Desktop\prg-basics\09-DictionariesStacksAndQueues\dogs.json', 'r', encoding='utf-8') as file:
#     content=json.load(file)


# for dog in content:
#     if dog["age"]<5:
#         print(f"Name: {dog["name"]}")
#         print(f"Age: {dog["age"]}")
#         print(f"Breed: {dog['breed']}")
#         print()  # Add an empty line for readability between dogs


import json

with open(r'C:\Users\Bartek\Desktop\prg-basics\09-DictionariesStacksAndQueues\dogs.json', 'r', encoding='utf-8') as file:
    content=json.load(file)


for dog in content:
    if dog['age']<5:
        print(f"Name: {dog['name']}")
        print(f"Age: {dog['age']}")
        print(f"Breed: {dog['breed']}")
        print()  # Dodanie pustej linii dla czytelności


