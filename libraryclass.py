class Book:
        def __init__(self, title, author, availability):
            self.title = title
            self.author = author
            self.availability = availability
        def check_out(self):
            self.availability = "unavailable"
        def return_book(self):
            self.availability = "available"
class Library:
    def __init__(self):
        self.book = []
    def add_book(self, book):
        self.book.append(book)
    def find_book(self, title):
         for book in self.book:
             if book.title == title:
                  print(book.title, book.author, book.availability)
                  return
         print("Book not found.")
    def show_availability(self):
        for book in self.book:
            print(f"{book.title}: {book.availability}")
lib = Library()
b1 = Book("Atomic Habits", "James Clear", "available")
b2 = Book("Zero to One", "Peter Thiel", "available")
lib.add_book(b1)
lib.add_book(b2)
lib.find_book("Atomic Habits")
lib.find_book("Harry Potter")
b1.check_out()
lib.show_availability()