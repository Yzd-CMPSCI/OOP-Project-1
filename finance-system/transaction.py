class Transaction:
    def __init__(self, transaction_id, transaction_type, amount, description, status="Pending"):
        self.transaction_id = transaction_id
        self.transaction_type = transaction_type
        self.amount = amount
        self.description = description
        self.status = status

    def process(self):
        if self.status == "Pending":
            self.status = "Processed"
            print(f"Transaction {self.transaction_id} processed successfully.")
        else:
            print(f"Cannot process transaction {self.transaction_id}: it is already {self.status}.")

    def cancel(self):
        if self.status == "Pending":
            self.status = "Cancelled"
            print(f"Transaction {self.transaction_id} cancelled successfully.")
        else:
            print(f"Cannot cancel transaction {self.transaction_id}: it is already {self.status}.")

    def update_description(self, new_description):
        self.description = new_description
        print(f"Description updated to: {self.description}")

    def display(self):
        print(
            f"ID: {self.transaction_id} | Type: {self.transaction_type} | "
            f"Amount: ${self.amount:.2f} | Description: {self.description} | Status: {self.status}"
        )