class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def __getitem__(self, index):
        return self.books[index]


def main():
    library = Library()
    library.add_book(Book("1984", "Orwell"))
    library.add_book(Book("Brave New World", "Huxley"))

    print(library[0].title)  # Accessing the first book


if __name__ == "__main__":
    main()
