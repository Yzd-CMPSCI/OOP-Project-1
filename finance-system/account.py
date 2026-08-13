class Account:
    def __init__(self, account_number, account_type, balance, owner_name):
        self.account_number = account_number
        self.account_type = account_type
        self.balance = balance
        self.owner_name = owner_name

    def deposit(self, amount):
        self.balance += amount
        print(
            f"Deposited ${amount:.2f} to account {self.account_number}. New balance: ${self.balance:.2f}"
        )

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(
                f"Withdrew ${amount:.2f} from account {self.account_number}. New balance: ${self.balance:.2f}"
            )
        else:
            print(
                f"Cannot withdraw ${amount:.2f} from account {self.account_number}: insufficient funds. Current balance: ${self.balance:.2f}"
            )

    def display_account(self):
        print(
            f"Account {self.account_number}: {self.account_type} | Owner: {self.owner_name} | Balance: ${self.balance:.2f}"
        )