import json

with open(r'C:\Users\Bartek\Desktop\prg-basics\09-DictionariesStacksAndQueues\reservations.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
    # Pobierz listę rezerwacji z klucza "reservations"
reservations=data['reservations']
    
def count_of_rooms(reservations):
    return len(reservations)

def count_paid_unpaid_reservations(reservations):
    paid = sum(1 for reservation in reservations if reservation['paid'])
    unpaid = len(reservations) - paid
    return paid, unpaid

def calculate_total_values(reservations):
    total_paid = sum(reservation['nights']*reservation['price_per_night'] for reservation in reservations if reservation['paid'])
    total_unpaid = sum(reservation['nights']*reservation['price_per_night'] for reservation in reservations if not reservation['paid'])
    return total_paid, total_unpaid
def print_summary(reservations):
    num_of_rooms=count_of_rooms(reservations)
    paid,unpaid=count_paid_unpaid_reservations(reservations)
    total_paid, total_unpaid = calculate_total_values(reservations)

    print(f"Liczba pokoi: {num_of_rooms}")
    print(f"Liczba płatnych rezerwacji: {paid}")
    print(f"Liczba niepłatnych rezerwacji: {unpaid}")
    print(f"Łączna wartość płatnych rezerwacji: {total_paid:.2f} zł")
    print(f"Łączna wartość niepłatnych rezerwacji: {total_unpaid:.2f} zł")

print_summary(reservations)



