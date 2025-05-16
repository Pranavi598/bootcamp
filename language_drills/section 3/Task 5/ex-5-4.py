class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    @classmethod
    def from_json(cls, data):
        """Alternative constructor to create a Book instance from a dictionary"""
        return cls(data["title"], data["author"])

    @classmethod
    def from_dict(cls, data):
        """Another alternative constructor to create a Book instance from a dict"""
        return cls(data["title"], data["author"])

    def __str__(self):
        return f"Book: {self.title} by {self.author}"

def main():
    # Creating Book instance using from_json method
    book_data = {"title": "Fahrenheit 451", "author": "Ray Bradbury"}
    book1 = Book.from_json(book_data)
    print(book1)  # Output: Book: Fahrenheit 451 by Ray Bradbury

    # Creating Book instance using from_dict method
    book_dict = {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald"}
    book2 = Book.from_dict(book_dict)
    print(book2)  # Output: Book: The Great Gatsby by F. Scott Fitzgerald

if __name__ == "__main__":
    main()
