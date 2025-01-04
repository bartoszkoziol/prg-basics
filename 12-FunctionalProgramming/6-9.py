measurements={"Krakow":7,"Warszawa":-2,"Sopot":4,"Koszalin":-1,"Opole":3}

valid_cities=list(filter(lambda x:x[1]>=0, measurements.items()))

city_names=[city for city,temp in valid_cities]
print("Cities with positive temp: ", ", ".join(city_names))