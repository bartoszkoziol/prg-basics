def f(sentence):
    no_space_sentence=""
    for char in sentence:
        if char != " ":
            no_space_sentence+=char
        else:
            continue
    return no_space_sentence

            
print(f("integrated development environment"))
print(f("A programming language is a system of notation for writingcomputer programs"))
    