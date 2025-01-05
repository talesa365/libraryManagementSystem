class Book:
    def __init__(self, title, author,book_id):
        self.title = title
        self.author = author
        self.book_id = id
        self.is_available = True

    def display_info(self):
        """Return information about the book."""
        availability = "Available" if self._is_available else "Not Available"
        return f"Title: {self.title}, Author: {self.author}, Status: {availability}"

    def borrow_book(self):
        """Mark the book as borrowed if available."""
        if self._is_available:
            self._is_available = False
            return True
        return False

    def return_book(self):
        """Mark the book as available."""
        self._is_available = True


class Library:
    def __init__(self):
        self.books = {}
        self.next_id = 1

    def add_book(self,title,author):#each time a book is added it gets stored in the self.books line 27 and self.books increments
        book = Book(self.next_id,title,author)
        self.books[self.next_id] = book
        return book
    def get_all_books(self):
        return list(self.books.values())#displays only what is in the list of books on line 27
    
    def delete_book(self,book_id):
        if book_id in self.books:
            del self.books[book_id]
            return True
        return False #if it is not in the book_id it will return false

