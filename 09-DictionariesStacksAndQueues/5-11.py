import json

file_path="voting.json"
try: 
    with open(file_path, 'r', encoding='utf-8') as file:
        content=json.load(file)
except FileNotFoundError:
    content={}

name =  input("Enter name to vote: ").strip()

if name in content:
    content[name]+=1
else:
    content[name]=1


with open(file_path, 'w') as file:
    json.dump(content, file, indent=4)

print(f"Zapisano głoś na {name}")

