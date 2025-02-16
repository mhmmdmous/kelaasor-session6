class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class Library:
    def __init__(self):
        self.dict_books = {}

    
    def add_book(self, book):
        self.dict_books[book.title] = book.author
    
    def list_books(self):
        for keys, values in self.dict_books.items():
            print(f"{keys} by {values}.")
    
Library = Library()
Library.add_book(Book("1984", "George Orwell"))  
Library.add_book(Book("To Kill a Mockingbird", "Harper Lee"))  
Library.list_books()


        