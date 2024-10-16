class Resource:
    def __init__(self, title: str, deposit: int, barcode: int, location: tuple):
        self.title = title
        self.deposit = deposit
        self.barcode = barcode  # Each Resource instance is unique and has its own barcode
        self.location = location  # Tuple representing (beam, shelf, level)
        self.available = True  # Resource availability status
        self.loan_history = []  # Store loan history for this specific copy

    def is_available(self):
        return self.available

    def set_available(self, available: bool):
        self.available = available

    def add_loan_to_history(self, user_name: str, loan_date: str, return_date: str):
        self.loan_history.append((user_name, loan_date, return_date))

    def get_loan_history(self):
        return self.loan_history

    def __repr__(self):
        return f"Resource(title={self.title}, deposit={self.deposit}, barcode={self.barcode}, available={self.available})"

    def __str__(self):
        return f"Resource: {self.title} (Barcode: {self.barcode}), Deposit: {self.deposit}, Available: {self.available}"
