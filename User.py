from typing import Dict, List
from Resource import Resource
from Loan import Loan

class User:
    def __init__(self, name: str, deposit: int):
        self.__name = name
        self.__deposit = deposit
        self.__can_borrow = True
        self.__loans: Dict[int, Loan] = {}  # Store loans by resource barcode
        self.__loans_history = []

    def get_name(self):
        return self.__name

    def set_name(self, name: str):
        self.__name = name

    def get_loans(self):
        return list(self.__loans.values())

    def set_can_borrow(self, status: bool):
        self.__can_borrow = status

    def can_borrow_status(self):
        # Update borrowing status based on current loans
        for loan in self.__loans.values():
            if loan.is_overdue():
                self.__can_borrow = False
                return False
        self.__can_borrow = True
        return True

    def add_loan(self, loan: Loan):
        if not self.can_borrow_status():
            print(f"{self.__name} cannot borrow more resources due to overdue loans.")
            return False

        if loan.resource.deposit > self.__deposit:
            print(f"{self.__name} does not have enough deposit to borrow {loan.resource.title}.")
            return False

        self.__loans[loan.resource.barcode] = loan
        self.__deposit -= loan.resource.deposit
        self.__loans_history.append((loan.resource.title, loan.loan_date))
        print(f"{self.__name} borrowed {loan.resource.title}.")
        return True

    def return_loan(self, resource: Resource):
        if resource.barcode in self.__loans:
            loan = self.__loans.pop(resource.barcode)
            self.__deposit += loan.resource.deposit
            resource.set_available(True)
            resource.add_loan_to_history(self.__name, loan.loan_date, loan.return_date)
            print(f"{self.__name} returned {resource.title}.")
        else:
            print(f"{self.__name} does not have {resource.title} on loan.")

    def display_loan_history(self):
        if not self.__loans_history:
            print(f"{self.get_name()} has no loan history.")
        else:
            print(f"Loan history for {self.get_name()}:")
            for title, loan_date in self.__loans_history:
                print(f"Resource: {title}, Loan Date: {loan_date}")

    def __repr__(self):
        return f"User(name={self.__name}, deposit={self.__deposit})"

    def __str__(self):
        return f"User - name: {self.__name}, deposit: {self.__deposit}, can borrow: {self.__can_borrow}"
