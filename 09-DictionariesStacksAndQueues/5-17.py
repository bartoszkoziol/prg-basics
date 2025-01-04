import json

# Open the JSON file in read mode
with open(r'C:\Users\Bartek\Desktop\prg-basics\09-DictionariesStacksAndQueues\cities.json', 'r', encoding='utf-8') as file:
   # Load the data from the JSON file into a variable
   data = json.load(file)

# Print the JSON data
for city in data:
   for key , val in city.items():
      print(key,':',val)
   print()

