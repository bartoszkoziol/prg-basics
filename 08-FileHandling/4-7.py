import re

text = input("Enter your text: ")

vowel_pattern = r"[aeiouAEIOU]"

vowels = re.findall(vowel_pattern, text)

num_vowels = len(vowels)

print("Vowels in the text: ", num_vowels)

