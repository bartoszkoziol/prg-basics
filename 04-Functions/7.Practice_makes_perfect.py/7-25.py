def f(text):
    formated_text1=""
    formated_text2=""
    for letter in text:
        formated_text1+=letter+"-"
        formated_text2=formated_text1[:-1]
    return formated_text2

print(f("University"))  # Output: "U-n-i-v-e-r-s-i-t-y"
print(f("UE"))          # Output: "U-E"
print(f("x"))           # Output: "x"
print(f(""))            # Output: ""