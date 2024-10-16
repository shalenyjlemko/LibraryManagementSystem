from Resource import Resource
from datetime import datetime

class Magazine(Resource):
    def __init__(self, title, volume, publication, deposit, barcode, location):
        super().__init__(title, deposit, barcode, location)
        self.volume = volume
        self.publication = datetime.strptime(publication, "%d/%m/%y")

    def __repr__(self):
        return f"Magazine(title={self.title}, volume={self.volume}, publication={self.publication}, deposit={self.deposit})"

    def __str__(self):
        return f"Magazine - title: {self.title}, volume: {self.volume}, publication: {self.publication.strftime('%d/%m/%y')}, deposit: {self.deposit}"
