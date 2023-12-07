from Book import *
from LibraryManagementSystem import *


if __name__ == "__main__":
    library_system = LibraryManagementSystem()
    library_system.initialize_catalog()

    library_system.display_catalog()
    library_system.checkout_books()
    library_system.display_checked_out_books()
    library_system.return_books()
