class Book:
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
    # Class method to create an instance from string
    book_str = "Brave New World|Aldous Huxley"
    book = Book.from_string(book_str)
    print(book)  # Output: Book: Brave New World by Aldous Huxley

if __name__ == "__main__":
    main()
