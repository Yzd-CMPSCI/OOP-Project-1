from client import Client
from account import Account
from transaction import Transaction
from branch import Branch


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
