class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def __len__(self):
        return len(self.books)


def main():
    library = Library()
    library.add_book(Book("1984", "Orwell"))
    library.add_book(Book("Brave New World", "Huxley"))

    print(len(library))  # Calls __len__()


if __name__ == "__main__":
    main()
