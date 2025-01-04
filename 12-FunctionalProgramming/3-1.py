# def eur_to_pln(amount):
#     pln_val=amount/4.5
#     return pln_val

an_func= lambda amount: amount/4.5

eur_transactions=[15.90, 38.47, 4.07, 132.70, 9.15]
calculate_amount=list(map(an_func,eur_transactions))

for am in calculate_amount:
    print(f"{am:.2f}")