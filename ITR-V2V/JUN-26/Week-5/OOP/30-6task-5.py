class Book:
    shelves = 5

    def __init__(self,title):
        self.title = title

book1 = Book("Python 101")
book2 = Book("Java Basics")

print(f"Title of Book 1 : {book1.title},\nTitle of Book 2 : {book2.title}")
print(f"Number of shelves in library : {Book.shelves}")