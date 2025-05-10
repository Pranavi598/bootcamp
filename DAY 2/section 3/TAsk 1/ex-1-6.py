class Book:
    def __init__(self, title="Untitled", author="Unknown"):
        self.title = title
        self.author = author

def main():
    book1 = Book("1984", "Orwell")
    book2 = Book()  # Using default values

    print(f"Book 1: Title = {book1.title}, Author = {book1.author}")
    print(f"Book 2: Title = {book2.title}, Author = {book2.author}")

if __name__ == "__main__":
    main()
