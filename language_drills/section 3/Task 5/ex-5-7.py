class Book:
    @staticmethod
    def is_valid_isbn(isbn):
        """Static method to validate ISBN format"""
        return isbn.isdigit() and len(isbn) == 13

    def __init__(self, title, author):
        self.title = title
        self.author = author

    @classmethod
    def from_string(cls, s):
        """Class method to create a Book instance from a string like 'Title|Author'"""
        title, author = s.split('|')
        return cls(title, author)

    def __str__(self):
        return f"Book: {self.title} by {self.author}"

class EBook(Book):
    @staticmethod
    def is_valid_isbn(isbn):
        """Overridden static method to validate ISBN format"""
        return isbn.isdigit() and len(isbn) == 13

def main():
    # Static method invocation from Book class
    print(Book.is_valid_isbn("1234567890123"))  # True

    # Static method invocation from EBook class
    print(EBook.is_valid_isbn("1234567890123"))  # True

if __name__ == "__main__":
    main()
