###
# String manipulation
#

movie = "The Lord of the Rings: The Return of the King"

# display number of characters
print('Number of characters: ', len(movie))

#upper(movie) powinno być movie.upper() – metoda upper() musi być wywołana na obiekcie movie, a nie jako osobna funkcja.
#lower(movie) powinno być movie.lower() – analogicznie jak w przypadku upper().


# display title in capital letters
print("Title in capital letters: ", movie.upper())

# display title in small letters
print("Title in lower case: ", movie.lower())

# display how many times the vowel "e" appears in the title
print("This is how many times the vowel e appears in the title: ", movie.count("e"))

# display where in the text is the word "Lord"
lord_positon = movie.rfind("Lord")
print("The word Lord is found at index: ", lord_positon)

# display where in the text is the word "dragon"
dragon_position = movie.rfind("dragon")
if dragon_position != -1:
    print("The word dragon is found at index: ", dragon_position)
else:
    print("The is no 'dragon' word in this text")