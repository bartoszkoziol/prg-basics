# # def num_of_letters(text):
# #     return [len(word) for word in text.split()]


# text = "I completely agree with you"
# # num_of_letters = lambda text: len(word) for word in text   #żle!
# num_of_letters = lambda word: len(word)


text = "I completely agree with you"

result = list(map(lambda word: len(word), text.split()))

print(result)