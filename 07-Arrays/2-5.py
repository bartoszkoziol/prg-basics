# 5x5 cinema seating
# A = Available, B = Booked
cinema_seats = [
   ['A', 'A', 'B', 'A', 'A'],
   ['A', 'B', 'B', 'A', 'A'],
   ['A', 'A', 'A', 'A', 'B'],
   ['B', 'A', 'A', 'A', 'A'],
   ['A', 'B', 'A', 'A', 'A']
]

def seats_total(cinema_seats):
   return sum(len(row) for row in cinema_seats)

def seats_available(cinema_seats):
   return sum(row.count("A") for row in cinema_seats)

def seats_booked(seats):
   return sum(row.count("B") for row in cinema_seats)

def seat_status(cinema_seats, row, place): 
   return cinema_seats[row-1][place-1]

print('CINEMA INFORMATION TABLE')
print('Total seats:', seats_total(cinema_seats))
print('Seats available:',seats_available(cinema_seats))
print('Seats booked:', seats_booked(cinema_seats))
print('Seat in row 1, place 1:', seat_status(cinema_seats, 1, 1))
print('Seat in row 5, place 5:', seat_status(cinema_seats, 5, 5))
print('Seat in row 3, place 5:', seat_status(cinema_seats, 3, 5))