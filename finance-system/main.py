from client import Client
from account import Account
from transaction import Transaction
from branch import Branch

# Self Reminder to TEST THIS B4 Code Review pls!!!! 
# Create three clients
client_1 = Client(1, "Alice", "alice@email.com", "0411111111")
client_2 = Client(2, "Bob", "bob@email.com", "0422222222")
client_3 = Client(3, "Charlie", "charlie@email.com", "0433333333")

print("\nClients before changes:")
client_1.display_summary()
client_2.display_summary()
client_3.display_summary()

client_1.update_contact(email="newalice@email.com")
client_2.update_contact(phone="0499999999")

print("\nClients after changes:")
client_1.display_summary()
client_2.display_summary()
client_3.display_summary()


# Create three accounts
account_1 = Account("A101", "Savings", 500, "Alice")
account_2 = Account("A102", "Everyday", 1000, "Bob")
account_3 = Account("A103", "Savings", 200, "Charlie")

print("\nAccounts before changes:")
account_1.display_account()
account_2.display_account()
account_3.display_account()

account_1.deposit(100)
account_2.deposit(200)

account_1.withdraw(50)
account_2.withdraw(100)
account_3.withdraw(500)  # This should fail

print("\nAccounts after changes:")
account_1.display_account()
account_2.display_account()
account_3.display_account()

# Create three transactions
transaction_1 = Transaction(1, "Deposit", 100, "Cash deposit")
transaction_2 = Transaction(2, "Withdrawal", 50, "ATM withdrawal")
transaction_3 = Transaction(3, "Transfer", 200, "Money transfer")

print("\nTransactions before changes:")
transaction_1.display()
transaction_2.display()
transaction_3.display()

transaction_1.process()
transaction_2.cancel()
transaction_3.update_description("Transfer to savings")

# Show that completed transactions cannot be changed
transaction_1.cancel()
transaction_2.process()

print("\nTransactions after changes:")
transaction_1.display()
transaction_2.display()
transaction_3.display()


# Create three branches
branch_1 = Branch(1, "City Branch", "Sydney", "02 1111 1111")
branch_2 = Branch(2, "North Branch", "Newcastle", "02 2222 2222", True)
branch_3 = Branch(3, "West Branch", "Adelaide", "08 3333 3333")

print("\nBranches before changes:")
branch_1.display_branch()
branch_2.display_branch()
branch_3.display_branch()

branch_1.open_branch()
branch_2.close_branch()
branch_3.update_phone("08 9999 9999")

print("\nBranches after changes:")
branch_1.display_branch()
branch_2.display_branch()
branch_3.display_branch()