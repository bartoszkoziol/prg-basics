file_name = r'C:\Users\Bartek\Desktop\prg-basics\08-FileHandling\pets.txt'

total_word_count=0

with open(file_name, 'r') as file:
    for line in file:
        print(line.strip())
        words=line.split()
        total_word_count+=len(words)
print(f"Total number of words: {total_word_count}")
