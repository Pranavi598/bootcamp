class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

def main():
    book1 = Book("1984", "Orwell")  # Create an object of the Book class
    print(f"Title: {book1.title}, Author: {book1.author}")

if __name__ == "__main__":
    main()
