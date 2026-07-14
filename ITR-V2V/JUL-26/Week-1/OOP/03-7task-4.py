#Create a "Library" class with a private "__books" attribute and methods to issue and return books.
class Library:
    def __init__(self, books):
        self.__books = books 

    def ShowBooks(self):
        if self.__books:
            print("Available books:")

            for book in self.__books:
                print(f"- {book}")

        else:
            print("No books available in the library.")

    def issuedBook(self, bookName):
        if bookName in self.__books:
            self.__books.remove(bookName)
            print(f'Book "{bookName}" has been issued.')

        else:
            print(f'Sorry, "{bookName}" is not available.')

    def return_book(self, bookName):
        self.__books.append(bookName)
        print(f'Book "{bookName}" has been returned.')

lib = Library(["Advance Java", "Python ", "C Programming"])
lib.ShowBooks()
lib.issuedBook("Python Basics")
lib.ShowBooks()
lib.return_book("Python Basics")
lib.ShowBooks()
