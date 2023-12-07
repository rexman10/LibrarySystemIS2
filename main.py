from datetime import datetime, timedelta
from typing import Dict

class Book:
    def __init__(self, code, title, author, availability):
        self.code = code
        self.title = title
        self.author = author
        self.availability = availability

    def __str__(self):
        return f"Book{{code='{self.code}', title='{self.title}', author='{self.author}', availability={self.availability}}}"

class LibraryManagementSystem:
    MAX_BOOKS_PER_CHECKOUT = 10
    LATE_FEE_PER_DAY = 1.0

    def __init__(self):
        self.catalog = {}
        self.checked_out_books = {}

    def initialize_catalog(self):
        self.catalog["001"] = Book("001", "Java Programming", "John Doe", 5)
        self.catalog["002"] = Book("002", "Introduction to Algorithms", "Jane Smith", 3)
        self.catalog["003"] = Book("003", "Database Management", "Alan Johnson", 2)

    def display_catalog(self):
        print("Available Books Catalog:")
        for book in self.catalog.values():
            print(book)

    def checkout_books(self):
        print("Enter the book codes you want to checkout (comma-separated):")
        input_codes = input().split(',')

        for code in input_codes:
            code = code.strip()
            if code not in self.catalog:
                print(f"Error: Book with code {code} not found.")
                return

            print(f"Enter the quantity for book {code}:")
            quantity = self.read_positive_integer()

            if quantity > self.MAX_BOOKS_PER_CHECKOUT:
                print(f"Error: Maximum books per checkout is {self.MAX_BOOKS_PER_CHECKOUT}")
                return

            self.checked_out_books[code] = quantity

        self.display_checkout_summary()

    def display_checkout_summary(self):
        print("Checkout Summary:")
        for code, quantity in self.checked_out_books.items():
            book = self.catalog[code]
            due_date = datetime.now() + timedelta(days=14)
            late_fee = self.calculate_late_fee(due_date)

            print(f"Book Code: {book.code}, Title: {book.title}, Quantity: {quantity}, Due Date: {due_date}, Late Fee: ${late_fee}")

        print("Do you want to confirm the checkout? (Y/N)")
        confirmation = input().strip().upper()

        if confirmation != "Y":
            print("Checkout canceled.")
            self.checked_out_books.clear()

    def return_books(self):
        print("Enter the book codes you want to return (comma-separated):")
        input_codes = input().split(',')

        total_late_fees = 0.0

        for code in input_codes:
            code = code.strip()
            if code not in self.checked_out_books:
                print(f"Error: Book with code {code} not found in checked-out books.")
                return

            book = self.catalog[code]
            quantity = self.checked_out_books[code]

            # Assuming a simple return without checking due dates
            late_fee = self.calculate_late_fee(datetime.now())
            total_late_fees += late_fee

            # Update the availability of the book in the catalog
            book.availability += quantity

        print("Return Summary:")
        print(f"Total Late Fees Incurred: ${total_late_fees}")

    def display_checked_out_books(self):
        print("Books Checked Out:")
        for code, quantity in self.checked_out_books.items():
            book = self.catalog[code]
            print(f"Book Code: {book.code}, Title: {book.title}, Quantity: {quantity}")

    def read_positive_integer(self):
        while True:
            try:
                input_value = int(input().strip())
                if input_value > 0:
                    return input_value
                else:
                    print("Error: Please enter a positive integer greater than zero.")
            except ValueError:
                print("Error: Please enter a valid integer.")

    def calculate_late_fee(self, due_date):
        days_late = (datetime.now() - due_date).days
        return max(0, days_late) * self.LATE_FEE_PER_DAY

if __name__ == "__main__":
    library_system = LibraryManagementSystem()
    library_system.initialize_catalog()

    library_system.display_catalog()
    library_system.checkout_books()
    library_system.display_checked_out_books()
    library_system.return_books()
