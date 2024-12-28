categories = ["Food", "Transport", "Rent", "Entertainment"]
expenses = [500, 150, 1000, 200]

max_expenses = max(expenses)  #znajduje najwieksza wartosc
max_index = expenses.index(max_expenses) #zwraca index najwiekszej wartosci

most_expensive_category = categories[max_index] #zwraca odpowiadajaca indexowi najwiekszego wydatku odpowiedni wydatek

print(f"The most expensive category is {most_expensive_category} with an expense of {max_expenses}")

