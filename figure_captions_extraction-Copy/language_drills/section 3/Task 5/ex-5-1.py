class Book:
    @staticmethod
    def is_valid_isbn(isbn):
        """Static method to validate ISBN format"""
        return isbn.isdigit() and len(isbn) == 13

def main():
    # Static method invocation
    print(Book.is_valid_isbn("1234567890123"))  # True
    book_instance = Book()
    print(book_instance.is_valid_isbn("1234567890123"))  # True

if __name__ == "__main__":
    main()
