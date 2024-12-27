
names_unsorted = [
   'James',
   'Emily',
   'William',
   'Olivia',
   'Benjamin',
   'Sophia',
   'Henry']

names_sorted = sorted(names_unsorted, key=len)
# print(names_sorted)
for name in names_sorted:
    print(name)