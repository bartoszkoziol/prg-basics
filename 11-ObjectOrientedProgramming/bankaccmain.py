from classbankacc import Bankaccount

def main():

    bank_account=Bankaccount("12 3456 5555 9090 1111 0000 7722")

    bank_account.display_info()

    bank_account.deposit(25.30)

    bank_account.display_info()

    bank_account.withdraw(31.70)

    bank_account.display_info()

    bank_account.withdraw(14)

    bank_account.display_info()

main()