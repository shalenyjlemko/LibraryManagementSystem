from Library import Library
from Book import Book
from Magasine import Magazine

# Initialize library
library = Library()

# Add some users
user1 = library.add_user("Alice", 100)
user2 = library.add_user("Bob", 50)

# Add a book resource
book1 = Book(
    title="Python Programming",
    author="John Doe",
    isbn="1234567890",
    deposit=10,
    barcode=101,
    location=(1, 2, 3)
)
library.add_resource(book1)

# Add a magazine resource
magazine1 = Magazine(
    title="Nature",
    volume="42",
    publication="15/10/24",
    deposit=5,
    barcode=102,
    location=(2, 3, 1)
)
library.add_resource(magazine1)

# Borrow the book
library.borrow_resource("Alice", 101)  # Alice borrows the book

# Display all users and their loan status
library.display_all_users()

# Display all resources
library.display_all_resources()

# Alice returns the book
library.return_resource("Alice", 101)

# Check resources and user status again
library.display_all_users()
library.display_all_resources()
