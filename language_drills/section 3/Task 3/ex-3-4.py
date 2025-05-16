class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __lt__(self, other):
        return self.title < other.title

def main():
    book1 = Book("1984", "Orwell")
    book2 = Book("Brave New World", "Huxley")
    book3 = Book("Fahrenheit 451", "Bradbury")

    books = [book1, book2, book3]
    books.sort()  # Sorting using __lt__()

    for book in books:
        print(book.title)

if __name__ == "__main__":
    main()
