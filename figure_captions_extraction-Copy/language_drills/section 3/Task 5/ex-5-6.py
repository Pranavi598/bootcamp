class Book:
    @staticmethod
    def is_valid_isbn(isbn):
        """Static method to validate ISBN format"""
        return isbn.isdigit() and len(isbn) == 13

    @classmethod
    def from_string(cls, s):
        """Class method to create a Book instance from a string like 'Title|Author'"""
        title, author = s.split('|')
        return cls(title, author)

    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book: {self.title} by {self.author}"

def main():
    # Static method invocation from class
    print(Book.is_valid_isbn("1234567890123"))  # True

    # Class method invocation from class
    book_str = "Brave New World|Aldous Huxley"
    book = Book.from_string(book_str)
    print(book)  # Output: Book: Brave New World by Aldous Huxley

if __name__ == "__main__":
    main()
