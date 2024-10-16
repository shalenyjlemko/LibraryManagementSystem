from typing import Dict, List
from User import User
from Resource import Resource
from Loan import Loan
from Book import Book
from Magasine import Magazine


class Library:
    def __init__(self):
        self.users: Dict[str, User] = {}  # Stores users by name
        self.resources: Dict[int, Resource] = {}  # Stores resources by barcode
        self.loans: List[Loan] = []  # All active loans
    
    def add_user(self, name: str, deposit: int) -> User:
        
        user = User(name, deposit)
        self.users[name] = user
        print(f"User {name} registered with a deposit of {deposit}.")
        return user

    def add_resource(self, resource: Resource):
        
        self.resources[resource.barcode] = resource
        print(f"Added resource: {resource.title} (Barcode: {resource.barcode})")

    def search_resource(self, title: str) -> List[Resource]:
        """Search for resources by title."""
        results = [res for res in self.resources.values() if res.title.lower() == title.lower() and res.is_available()]
        print(f"Found {len(results)} available resources with title '{title}'.")
        return results

    def borrow_resource(self, user_name: str, resource_barcode: int):
        
        user = self.users.get(user_name)
        resource = self.resources.get(resource_barcode)

        if not user:
            print(f"No user found with the name {user_name}.")
            return

        if not resource:
            print(f"No resource found with barcode {resource_barcode}.")
            return

        if not resource.is_available():
            print(f"The resource {resource.title} is currently unavailable.")
            return

        loan = Loan(user, resource)
        user.add_loan(loan)
        resource.set_available(False)
        self.loans.append(loan)
        print(f"{user_name} borrowed {resource.title}.")

    def return_resource(self, user_name: str, resource_barcode: int):
        
        user = self.users.get(user_name)
        resource = self.resources.get(resource_barcode)

        if not user or not resource:
            print(f"Invalid user or resource for return operation.")
            return

        user.return_loan(resource)
        print(f"{user_name} returned {resource.title}.")
    
    def display_all_users(self):
        
        for user in self.users.values():
            print(user)

    def display_all_resources(self):
        
        for resource in self.resources.values():
            print(resource)
