from datetime import datetime, timedelta
from Resource import Resource
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from User import User

class Loan:
    def __init__(self, user: 'User', resource: Resource):
        self.user = user
        self.resource = resource
        self.loan_date = datetime.now()
        self.due_date = self.loan_date + timedelta(days=15)
        self.return_date = None  # Will be set when the resource is returned

    def update_current_date(self, new_date: datetime):
        self.current_date = new_date

    def mark_as_returned(self):
        self.return_date = datetime.now()

    def is_overdue(self) -> bool:
        """Check if the loan is overdue."""
        return datetime.now() > self.due_date and self.return_date is None

    def __repr__(self):
        return f"Loan(user={self.user.get_name()}, resource={self.resource.title}, loan_date={self.loan_date}, due_date={self.due_date}, return_date={self.return_date})"

    def __str__(self):
        status = "Returned" if self.return_date else "Active"
        return f"Loan for {self.resource.title} to {self.user.get_name()} (Status: {status})"
