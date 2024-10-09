class Book:
    def __init__(self,title:str,author:str):
        self.title = title
        self.author = author

class EBook(Book):
    def __init__(self,file_size:int):
        super().__init__(title,author)
        self.file_size = file_size

class PrintBook(Book):
    def __init__(self,page_count:int):
        super().__init__(title,author)
        self.page_count = page_count
class Library:
    def __init__(self):
        self.books = []  # List to store books of all types

    def add_book(self, book):
        if isinstance(book, Book):
            self.books.append(book)
        else:
            print("Error: Only instances of Book, EBook, or PrintBook can be added.")

    def list_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            print("Listing all books in the library:")
            for book in self.books:
                print(book)
