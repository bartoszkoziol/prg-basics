price_list = {
   'T-shirt': 19.99,
   'Jeans': 49.99,
   'Jacket': 89.99,
   'Sneakers': 59.99,
   'Hat': 15.99
}

# print("Products prices before discount:")
# for name, price in price_list.items():
#     print(f"{name}: {price}")

# print("Total value before discount")
# total_sum_bfd=0
# for name, price in price_list.items():
#     total_sum_bfd+=price
# print(f"{total_sum_bfd:.2f}")

# # discount_rate=0.10
# # discounted_price_list={name: round(price*(1-discount_rate), 2) for name,price in price_list.items()}

# # for name, price in discounted_price_list.items():
# #     print(f"{name}: {price}")

# ###tutaj krócej:
# for name, number in price_list.items():
#     print(f"{name}: {number*0.9:.2f}")

# # total_sum_afd=0
# # for name, price in discounted_price_list.items():
# #     total_sum_afd+=price
# # print(f"{total_sum_afd:.2f}")

# ###tutaj krócej:
# total_sum_afd=0
# for name,price in price_list.items():
#     total_sum_afd+=price*0.9
# print(f"{total_sum_afd:.2f}")


print("Products prices before discount:")
for product, price in price_list.items():
    print(f"{product}: {price}")



for price in price_list.values():
    total_sum=0
    total_sum+=price
print(f"Total value before discount: {total_sum}")

for product, price in price_list.items():
    print(f"{product}: {price*0.9:.2f}")


total_sum_afd=0
for price in price_list.values():
    total_sum_afd+=price*0.9
print(total_sum_afd)