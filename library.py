class Book:#blueprint for creating a book for the lbrary
    def __init__(self, title, author, id):
        self.title = title
        self.author = author
        self.book_id = id
        self.is_available = True #idicates if the book can be borrowed

    def display_info(self):
        """Return information about the book to the user."""
        availability = "Available" if self._is_available else "Not Available"
        return f"Title: {self.title}, Author: {self.author}, Book id {self.book_id}, Status: {availability}"

    def borrow_book(self):
        """Mark the book as borrowed if available."""
        if self._is_available:
            self._is_available = False
            return True
        return False
    
     
    def is_available(self):
        if self.is_available:
            return f"This book is available"
        else:
            return f"This book is currently unavailable"


    def return_book(self):
        """Mark the book as available."""
        self._is_available = True



class Library:
    def __init__(self):#this method is called when a new library(book) object is created, initializes an empty container
        self.books = {}
        self.next_id = 1

    def add_book(self,title,author):#each time a book is added it gets stored in the self.books line 27 and self.books increments
        book = Book(self.next_id,title,author)
        self.books[self.next_id] = book
        return book
    def get_all_books(self):
        return list(self.books.values())#displays only what is in the list of books on line 27
    
    def get_book_by_id(self, book_id):
        if self.book_id:
            return f"Title: {self.title}, Author: {self.author}, Book id {self.book_id}
            else:
            return None
    
    def delete_book(self,book_id):
        if book_id in self.books:
            del self.books[book_id]
            return True
        return False #if it is not in the book_id it will return false
    
    class User:
        def __init__(self, name,user_id,borrowed_book):
            self.name = name
            self.user_id = user_id
            self.borrowed_book = borrowed_book

