def f(sentence):
    sentence2 = ""
    for char in sentence:
        if char != " ":
            sentence2 += char
        #elif char == " ":
            #continue
    return sentence2
            
print(f("integrated development environment"))
print(f("A programming language is a system of notation for writingcomputer programs"))
    