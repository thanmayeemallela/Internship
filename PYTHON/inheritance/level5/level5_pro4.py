class Book:
    def __init__(self, name):
        self.name = name

class SearchService:
    def search(self, name):
        print("Searching:", name)

class Library:
    def __init__(self):
        self.books = [Book("Python"), Book("SQL")]

    def find_book(self, search):
        search.search("Python")

library = Library()
print("Library HAS-A Books")
print("Library USES-A SearchService")
library.find_book(SearchService())
