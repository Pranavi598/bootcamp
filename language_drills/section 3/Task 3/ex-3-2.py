class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __eq__(self, other):
        if isinstance(other, Book):
            return self.title == other.title and self.author == other.author
        return False


def main():
    book1 = Book("1984", "Orwell")
    book2 = Book("1984", "Orwell")
    book3 = Book("Brave New World", "Huxley")

    print(book1 == book2)  # True
    print(book1 == book3)  # False


if __name__ == "__main__":
    main()
