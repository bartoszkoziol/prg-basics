def hotel_lists(hotels):
    return ", ".join(hotel["name"] for hotel in hotels)

def avg_price(hotels):
    total_price=sum(hotel["price"] for hotel in hotels)
    return round(total_price/len(hotels))

hotels_in_Krakow = [
   {"name":"Sky","price":320.00},
   {"name":"Metropol","price":480.00},
   {"name":"New Port","price":420.00},
   {"name":"Aparthotel","price":390.00}
]

hotels_in_Sopot = [
   {"name":"Focus","price":510.00},
   {"name":"Aqua","price":345.00},
   {"name":"La Boutique","price":390.00},
   {"name":"Marina","price":410.00}
]

krakow_names = hotel_lists(hotels_in_Krakow)
sopot_names = hotel_lists(hotels_in_Sopot)

krakow_prices = avg_price(hotels_in_Krakow)
sopot_prices = avg_price(hotels_in_Sopot)

cheaper_city = "Kraków" if krakow_prices<sopot_prices else "Sopot"

print(f"Hotels in Kraków: {krakow_names}")
print(f"Average hotel price in Krakow: {krakow_prices}")
print(f"Hotels in Sopot: {sopot_names}")
print(f"Average hotel price in Sopot: {sopot_prices}")
print(cheaper_city)