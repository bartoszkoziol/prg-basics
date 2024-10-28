from calendar_module import month_number
#n to numer miesiąca podany przez użytkownika 
def main():
    n = int(input("Podaj numer mieisąca (1-12): "))
    month_name = month_number(n)
    print(f"Miesiąc numer {n} to {month_name}")

if __name__ == "__main__":
    main()