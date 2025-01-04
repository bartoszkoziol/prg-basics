products_in_stock_and_prices = [(20,5.50),(15,8.30),(37,3.85),(4,11.60)]

total_value = sum(map(lambda item: item[0]*item[1], products_in_stock_and_prices))

print(total_value)