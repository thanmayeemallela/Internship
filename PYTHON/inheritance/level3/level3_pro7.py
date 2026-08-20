class SearchService:
    def search(self, word):
        print("Searching for:", word)

class Library:
    def find_book(self, search):
        search.search("Python")

Library().find_book(SearchService())
