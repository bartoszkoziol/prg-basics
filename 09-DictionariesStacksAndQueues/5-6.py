basic_data = {
   "name":"Barbara",
   "age":21
}

advanced_data = {
   "status":"student",
   "married":False,
   "interest":["reading","swimming"]
}

basic_data.update(advanced_data)
for key, value in basic_data.items():
    print(f"{key}: {value}")