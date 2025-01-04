from statisticclass import Statistics

def main():
    statistics = Statistics()

    statistics.add_number(12)
    statistics.add_number(37)
    statistics.add_number(6)
    statistics.add_number(9)
    statistics.add_number(17)

    statistics.display_numbers()    

    statistics.calculate_max()

    statistics.calculate_min()

    statistics.calculate_arithmetic_mean()

    statistics.calculate_median()

    statistics.print_statistics()

main()


