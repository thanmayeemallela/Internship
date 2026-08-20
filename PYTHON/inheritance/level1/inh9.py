class BankAccount:
    def show_balance(self):
        print("Balance: 10000")

class SavingsAccount(BankAccount):
    def save(self):
        print("Savings account")

class CurrentAccount(BankAccount):
    def business(self):
        print("Current account")

SavingsAccount().save()
SavingsAccount().show_balance()
CurrentAccount().business()
CurrentAccount().show_balance()
