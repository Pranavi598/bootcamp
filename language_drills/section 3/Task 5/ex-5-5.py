class Book:
    @staticmethod
    def is_valid_isbn(isbn):
        """Static method to validate ISBN format"""
        return isbn.isdigit() and len(isbn) == 13

    def __init__(self, title, author):
        self.title = title
        self.author = author

def main():
    # Static method invocation from class
    print(Book.is_valid_isbn("1234567890123"))  # True

    # Static method invocation from instance
    book = Book("1984", "George Orwell")
    print(book.is_valid_isbn("1234567890123"))  # True

if __name__ == "__main__":
    main()
