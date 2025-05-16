class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book: {self.title} by {self.author}"

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}')"


def main():
    book1 = Book("1984", "Orwell")

    print(book1)  # This calls __str__()
    print(repr(book1))  # This calls __repr__()


if __name__ == "__main__":
    main()
