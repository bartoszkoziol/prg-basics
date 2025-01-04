competitiono_results = [{"country":"Denmark","gold":2,"silver":4,"bronze":6},
{"country":"Finland","gold":5,"silver":0,"bronze":4},
{"country":"USA","gold":12,"silver":5,"bronze":11},
{"country":"Peru","gold":0,"silver":1,"bronze":7}]

valid_counutries = list(filter(lambda country: (country["gold"]+country["silver"]+country["bronze"])>=10, competitiono_results))
for country in valid_counutries:
    # print(f"{country['country']}: {country['gold'], country['silver'], country['bronze']}")\
    print(f"{country['country']}: {country['gold']}, {country['silver']}, {country['bronze']}")
