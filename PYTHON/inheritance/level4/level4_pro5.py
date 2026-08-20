class Book:
    def __init__(self, name):
        self.name = name

class Library:
    def __init__(self):
        self.books = [Book("Python"), Book("SQL")]

print("Library HAS-A Books")
for book in Library().books:
    print(book.name)
