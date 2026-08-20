class Book:
    def __init__(self, name):
        self.name = name

class Library:
    def __init__(self):
        self.books = [
            Book("Python"),
            Book("SQL"),
            Book("HTML")
        ]

    def show_books(self):
        for book in self.books:
            print(book.name)

Library().show_books()
