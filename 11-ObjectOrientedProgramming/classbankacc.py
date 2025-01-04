class Bankaccount:
    def __init__(self, account_number):
        self.account_number=account_number
        self.balancne=0

    def deposit(self, amount):
        if amount>0:
            self.balancne+=amount
            print(f"Deposited: {amount} PLN")
        else:
            print("Deposit amount must be positive")

    def withdraw(self, amount):
        if amount>self.balancne:
            print("Insufficient funds on the account")
        elif amount>0:
            self.balancne-=amount
            print(f"Withdrew: {amount} PLN")
        else:
            print("Withdrawal amount must be positive")

    def display_info(self):
        print(f"Bank Account number: {self.account_number}")
        print(f"Balance: {self.balancne}")


