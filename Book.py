from Resource import Resource

class Book(Resource):  # Corrected spelling of Resource
    def __init__(self, title, author, isbn, deposit, barcode, location):
        super().__init__(title, deposit, barcode, location)
        self.author = author
        self.isbn = isbn

    def __repr__(self):
        return f"Book(title={self.title}, author={self.author}, isbn={self.isbn}, deposit={self.deposit})"

    def __str__(self):
        return f"Book - title: {self.title}, author: {self.author}, ISBN: {self.isbn}, deposit: {self.deposit}"
