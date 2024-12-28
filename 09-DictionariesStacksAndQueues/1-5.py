countries = [
{"name":"Poland", "population":38000000},
{"name": "Germany", "population":83000000},
{"name": "France", "population":67000000},
{"name": "Italy", "population":60000000},
{"name": "Spain", "population":47000000}
]

print(f"{"COUNTRY":<15} {"POPULATION":>10}")

for country in countries:
    print(f"{country["name"]:<15} {country["population"]:>10}")