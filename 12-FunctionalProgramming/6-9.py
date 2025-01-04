measurements = {"Krakow":7,"Warszawa":-2,"Sopot":4,"Koszalin":-1,"Opole":3}

# results = list(filter(lambda temp: temp>0, measurements))
results = list(filter(lambda item: item[1]>0, measurements.items()))
# print(results)
cities_with_positive_temp=[city for city,temp in results]
for city in cities_with_positive_temp:
    print(city, end=" ")


