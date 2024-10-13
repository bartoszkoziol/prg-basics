###
# A program that reads temperature in degrees Celsius from the keyboard.
# Use comments to briefly describe the program's algorithm.
#

temp_w_celsjuszach = float(input("Podaj temperatuere w stopniach celsjusza: ")) #odczytujemy stopnie celsjusza podane przez uzytkownika



#przeliczanie temp z celsjusza na Fahrenheity
temp_w_fahrenheit = 32 + 9/5*temp_w_celsjuszach

#przeliczanie temp z celsjusza na Kelviny
temp_w_kelvinach = temp_w_celsjuszach + 273.15

#wyniki
print(f"Temperatura w stopniach Fahrenheita wynosi: {temp_w_fahrenheit}")
print(f"Temperatura w stopniach Kelvina wynosi: {temp_w_kelvinach}")