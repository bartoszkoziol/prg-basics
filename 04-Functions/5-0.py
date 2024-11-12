from calendar_module import month_number

def main():
    month_number_input = int(input("Podaj numer miesiąca: "))

    month_name = month_number(month_number_input)

    print(f"Nazwa miesiąca numer {month_number_input} to {month_name}")

if __name__ == "__main__":
    main()