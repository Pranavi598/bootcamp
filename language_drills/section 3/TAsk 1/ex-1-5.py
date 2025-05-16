class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def update_title(self, new_title):
        self.title = new_title  # Update the title

def main():
    book1 = Book("1984", "Orwell")
    print(f"Before Update: {book1.title}")
    book1.update_title("Animal Farm")  # Update the title
    print(f"After Update: {book1.title}")

if __name__ == "__main__":
    main()
