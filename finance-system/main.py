from client import Client
from account import Account
from transaction import Transaction
from branch import Branch

# Client test
client1 = Client(1, "Alice", "alice@email.com", "0412345678")
client1.display_summary()

# Account test
account1 = Account("A1001", "Savings", 500.0, "Alice")
account1.display_account()

# Transaction test
t1 = Transaction(1001, "Deposit", 150.0, "Salary payment")
t2 = Transaction(1002, "Withdrawal", 40.0, "Lunch")
t1.process()
t2.cancel()
t1.update_description("Monthly salary")
t1.display()
t2.display()

# Branch test
branch1 = Branch(101, "Main Branch", "Sydney", "555-1000")
branch2 = Branch(102, "North Branch", "Newcastle", "555-2000", True)
branch1.open_branch()
branch1.update_phone("555-1111")
branch1.display_branch()
branch2.display_branch()


