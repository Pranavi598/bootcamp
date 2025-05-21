class Book:
    category = "Fiction"  # Class variable

    def __init__(self, title, author):
        self.title = title
        self.author = author

def main():
    book1 = Book("1984", "Orwell")
    print(f"Category: {book1.category}")  # Accessing the class variable through the object

if __name__ == "__main__":
    main()
