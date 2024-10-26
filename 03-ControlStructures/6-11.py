#A computer program analyses the price of a product in an online store

price1=200
price2=140
discount_in_percentage=((price1-price2)/price1)*100


if discount_in_percentage>=10:
    print("Buy the product!")
    print(f"The discount is {discount_in_percentage}")
else:
    print("No significant price drop")
  
