import sys


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def describe(self):
        return f"'{self.title}' by {self.author}"


class Novel(Book):  # Subclassing Book
    def __init__(self, title, author, genre):
        super().__init__(title, author)
        self.genre = genre

    def describe(self):
        return f"Novel: {self.title} by {self.author}, Genre: {self.genre}"


def main():
    book1 = Book("1984", "Orwell")
    novel1 = Novel("Brave New World", "Huxley", "Dystopian")

    books = [book1, novel1]

    for book in books:
        print(book.describe())  # Polymorphism in action


if __name__ == "__main__":
    main()
