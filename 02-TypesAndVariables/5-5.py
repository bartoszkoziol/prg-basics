price1=input("Podaj cenę produktu przed rabatem:")
discount=input("Podaj wartość rabatu w %: ")
price1=float(price1)
discount=int(discount)

price_after_discount = price1 - price1*(discount/100)
price_diff = price1-price_after_discount

print(f"Cena produktu przed rabatem wynosi: {price1:.2f}")
print(f"Wartość rabatu wynosi: {discount}%")
print(f"Cena produktu po rabacie wynosi: {price_after_discount:.2f}")
print(f"Różnica między pierwotną ceną produktu a ceną po obniżce wynosi: {price_diff:.2f}")