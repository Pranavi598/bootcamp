class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

def main():
    book1 = Book("1984", "Orwell")
    book1.year_published = 1949  # Dynamically adding a new attribute
    print(f"Title: {book1.title}, Author: {book1.author}, Year: {book1.year_published}")

if __name__ == "__main__":
    main()
