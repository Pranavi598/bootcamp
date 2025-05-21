class Book:
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
    @classmethod
    def from_string(cls, s):
        """Overridden class method for EBook"""
        title, author = s.split('|')
        return cls(title, author, "5MB")  # Default file size for EBook

    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}"

def main():
    # Creating a Book instance from string
    book_str = "1984|George Orwell"
    book = Book.from_string(book_str)
    print(book)  # Output: Book: 1984 by George Orwell

    # Creating an EBook instance from string
    ebook_str = "Digital Fortress|Dan Brown"
    ebook = EBook.from_string(ebook_str)
    print(ebook)  # Output: EBook: Digital Fortress by Dan Brown, File Size: 5MB

if __name__ == "__main__":
    main()
