class Client:
    def __init__(self, client_id, name, email, phone, active=True):
        self.client_id = client_id
        self.name = name
        self.email = email
        self.phone = phone
        self.active = active

    def update_contact(self, email=None, phone=None):
        if email:
            self.email = email
        if phone:
            self.phone = phone

    def display_summary(self):
        print(
            f"Client {self.client_id}: {self.name} | Email: {self.email} | Phone: {self.phone} | Active: {self.active}"
        )