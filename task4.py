class Book:
    def __init__(self, title, author, year_published):
        self.title = title
        self.author = author
        self.year_published = year_published

    def describe(self):
        print(f"Title: {self.title}, Author: {self.author}, Year Published: {self.year_published}")


book1 = Book("THE WITCHER: THE LAST WISH", "Andrzej Sapkowski", 1993)
book2 = Book("THE LORD OF THE RINGS", "J.R.R. Tolkien", 1954)
book3 = Book("DUNE", "Frank Herbert", 1965)

book1.describe()
book2.describe()
book3.describe()