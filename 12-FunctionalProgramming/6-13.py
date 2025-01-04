import matplotlib.pyplot as plt

competition_results = [
    {"country": "Denmark", "gold": 2, "silver": 4, "bronze": 6},
    {"country": "Finland", "gold": 5, "silver": 0, "bronze": 4},
    {"country": "USA", "gold": 12, "silver": 5, "bronze": 11},
    {"country": "Peru", "gold": 0, "silver": 1, "bronze": 7}
]

#countries = list(map(competition_results["country"], competition_results))
countries = list(map(lambda x: x["country"], competition_results))
total_medals=list(map(lambda x: x["gold"]+x["silver"]+x["bronze"], competition_results))

plt.bar(countries, total_medals)

plt.title("Olympic Games Medal Clasification")
plt.xlabel("Countries")
plt.ylabel("Total medals")

plt.show()