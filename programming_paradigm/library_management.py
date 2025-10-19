class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def __str__(self):
        return f"{self.title} by {self.author}"

class Library:
    def __init__(self) -> None:
        self._books = []

    def add_book(self, book_obj):
        self._books.append(book_obj)
    
    def check_out_book(self, title):
        to_checkout = None
        for book in self._books:
            if book.title == title:
                to_checkout = book
                break
        if to_checkout == None:
            raise "Book not found"
        elif to_checkout._is_checked_out == True:
            raise "Book not available"
        else:
            to_checkout._is_checked_out = True
    
    def return_book(self, title):
        to_return = None
        for book in self._books:
            if book.title == title:
                to_return = book
                break
        if to_return == None:
            raise "Book not found"
        elif to_return._is_checked_out == False:
            raise "You cannot return a book that is not checked out"
        else:
            to_return._is_checked_out = False
    
    def list_available_books(self):
        for book in self._books:
            if book._is_checked_out == False:
                print(book)