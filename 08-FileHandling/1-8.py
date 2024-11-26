def read_from_file(name):
    with open(name, 'r') as file:
        content = file.read()
    return content

file_content = read_from_file("pets.txt")

file_lines = file_content.splitlines()

total_words = 0

for line in file_lines:
    words = line.split()  # Dzieli linię na słowa
    total_words += len(words)
#ctrl+? komentuje wszystko co zaznaczone
print(total_words)