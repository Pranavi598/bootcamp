class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def describe(self):
        return f"'{self.title}' by {self.author}"

class Novel(Book):  # Subclassing Book
    def __init__(self, title, author, genre):
        super().__init__(title, author)
        self.genre = genre

    def describe(self):
        return f"Novel: '{self.title}' by {self.author}, Genre: {self.genre}"

def main():
    book1 = Book("1984", "Orwell")
    novel1 = Novel("Brave New World", "Huxley", "Dystopian")

    # Polymorphism: Looping over both Book and Novel objects
    items = [book1, novel1]
    for item in items:
        print(item.describe())  # Different outputs based on the type of object

if __name__ == "__main__":
    main()
