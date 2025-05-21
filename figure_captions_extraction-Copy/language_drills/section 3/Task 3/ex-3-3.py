class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __eq__(self, other):
        return isinstance(other, Book) and self.title == other.title and self.author == other.author

    def __hash__(self):
        return hash((self.title, self.author))


def main():
    book1 = Book("1984", "Orwell")
    book2 = Book("1984", "Orwell")
    book3 = Book("Brave New World", "Huxley")

    books_set = {book1, book2, book3}
    print(len(books_set))  # Should print 2 (since book1 and book2 are equal)


if __name__ == "__main__":
    main()
