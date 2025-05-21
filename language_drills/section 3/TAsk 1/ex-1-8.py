def main():
    book1 = Book("1984", "Orwell")
    if isinstance(book1, Book):  # Check if book1 is an instance of Book class
        print(f"{book1.title} is a Book.")
    else:
        print(f"{book1.title} is not a Book.")

if __name__ == "__main__":
    main()
