import json

# Open the JSON file in read mode
with open(r'C:\Users\Bartek\Desktop\prg-basics\09-DictionariesStacksAndQueues\computer.json', 'r', encoding='utf-8') as file:
   # Load the data from the JSON file into a variable
   data = json.load(file)

# Print the JSON data
for key, value in data.items():
   print(key,':',value)

    