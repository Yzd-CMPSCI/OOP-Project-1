class Branch:
    def __init__(self, branch_number, branch_name, location, phone_number, is_open=False):
        self.branch_number = branch_number
        self.branch_name = branch_name
        self.location = location
        self.phone_number = phone_number
        self.is_open = is_open

    def open_branch(self):
        if self.is_open:
            print(f"Branch {self.branch_number} is already open.")
        else:
            self.is_open = True
            print(f"Branch {self.branch_number} opened.")

    def close_branch(self):
        if not self.is_open:
            print(f"Branch {self.branch_number} is already closed.")
        else:
            self.is_open = False
            print(f"Branch {self.branch_number} closed.")

    def update_phone(self, new_phone):
        self.phone_number = new_phone
        print(f"Branch {self.branch_number} phone updated to {self.phone_number}.")

    def display_branch(self):
        status = "Open" if self.is_open else "Closed"
        print(
            f"Branch {self.branch_number}: {self.branch_name} | "
            f"Location: {self.location} | Phone: {self.phone_number} | Status: {status}"
        )