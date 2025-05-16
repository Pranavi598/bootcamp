class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def describe(self):
        return f"'{self.title}' by {self.author}"

def main():
    book1 = Book("1984", "Orwell")
    print(book1.describe())  # Calling the method to get a formatted description

if __name__ == "__main__":
    main()
